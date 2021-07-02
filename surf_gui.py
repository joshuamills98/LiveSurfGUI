# Global Imports
import tkinter
import tkinter.font as TkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib import dates
import matplotlib.ticker as mticker
import numpy as np
import os

# Local Imports
from swell_analysis.swell_data_download import swell_data_main
from wind_analysis.wind_data_download import wind_data_main
from tools.compass import compass_reversal
from tools.color_converter import get_temp_colour


def convert_to_datetime(df):
    df = df.set_index(
        pd.to_datetime(df.iloc[:, 0],
                       format="%Y-%m-%d %H:%M:%S"))
    df = df.iloc[:, 1:]
    return df


def plot_on_axis(ax, data, name, c,
                 xticks_swell=False,
                 xticks_wind=False,
                 compass_change=False,
                 rolling_window=3):

    data.rolling(window=rolling_window).mean().plot(ax=ax,
                c=c,
                grid=True)

    ax.grid(alpha=0.5)
    ax.set_yticks(np.linspace(min(data),
                              max(data),
                              5))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax.set_xlabel('')
    ax.set_title(name)
    if xticks_swell or xticks_wind:
        if xticks_swell:
            # ax.set_xticklabels(ax.get_xticklabels(),
            #                    rotation=0,
            #                    ha='center')
            ticks_loc = ax.get_xticks().tolist()
            ax.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
            ax.xaxis.set_major_formatter(
                    dates.DateFormatter('%d\n%a'))
            ax.xaxis.set_tick_params(rotation=0,
                                     )
        # if xticks_wind:
            # ax.set_xticklabels(ax.get_xticklabels(),
            #                    rotation=0,
            #                    ha='center')
            # ax.xaxis.set_major_formatter(
            #         dates.DateFormatter('%a\n%H:%M'))
    else:
        ax.tick_params(
            axis='x',
            which='both',
            labelbottom=False
        )

    if compass_change:
        ax.set_yticklabels([compass_reversal[round(tick)] for
                            tick in ax.get_yticks()])


def place_swell_history():
    path = os.path.join("swell_analysis", "swell_data")
    data_fields = ['swell_height.csv',
                   'swell_period.csv',
                   'swell_direction.csv']
    swell_height = pd.read_csv(os.path.join(path, data_fields[0]))
    swell_period = pd.read_csv(os.path.join(path, data_fields[1]))
    swell_direction = pd.read_csv(os.path.join(path, data_fields[2]))
    swell_height = convert_to_datetime(swell_height).iloc[:, 1]
    swell_period = convert_to_datetime(swell_period).iloc[:, 0]
    swell_direction = convert_to_datetime(swell_direction).iloc[:, 0]
    fig, ax = plt.subplots(3, 1, figsize=(5, 6), dpi=100)

    plot_on_axis(ax=ax[0],
                 data=swell_height,
                 name='Swell Height (m)',
                 c='coral',
                 )

    plot_on_axis(ax=ax[1],
                 data=swell_period,
                 name='Swell Period (s)',
                 c='deepskyblue',
                 )

    plot_on_axis(ax=ax[2],
                 data=swell_direction,
                 name='Swell Direction',
                 c='palegreen',
                 xticks_swell=True,
                 compass_change=True,
                 )

    _ = fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=1, rowspan=5)
    # Plot last angle for swell direction
    plot_arrow(swell_direction[-1],
               row=1,
               column=0,
               image_path=os.path.join('swell_analysis',
                                       'images',
                                       'swell_arrow.png'),
               size=40*swell_height[-1])

    plot_swell_text(swell_height.index[-1],
                    swell_height[-1],
                    swell_period[-1],
                    swell_direction[-1])
    plt.close(fig)


def plot_arrow(angle, row, column, image_path, size):
    angle_calibrated = -90 - angle
    img = Image.open(image_path).rotate(angle_calibrated, expand=1).\
        resize((round(size), round(size)), Image.ANTIALIAS)
    arrow = ImageTk.PhotoImage(img)
    arrow_label = tkinter.Label(image=arrow)
    arrow_label.image = arrow
    arrow_label.grid(row=row, column=column, padx=1)


def plot_swell_text(time, height, period, angle):
    column = 0
    fontStyle = TkFont.Font(family="Lucida Grande", size=16)

    strtime = time.strftime("%a %H:%M")
    compass_direction = tkinter.Label(
        root,
        text="Swell Direction" + \
             "\n" + compass_reversal[angle] + \
             " ({})".format(str(angle)),
        font=fontStyle)

    swell_label = tkinter.Label(
        root,
        text="{:.2f} m \n @ {:.2f} seconds".format(height, period),
        font=fontStyle)

    date_format = tkinter.Label(
        root,
        text="Last Updated \n {}".format(strtime),
        font=fontStyle)

    date_format.grid(row=3, column=column, pady=0, padx=1)
    swell_label.grid(row=2, column=column, pady=0, padx=1)
    compass_direction.grid(row=0, column=column, pady=0, padx=1)


# Wind plots:


def plot_wind_history(location):
    csv_name = location.replace(' ', '_') + '_Wind_Data.csv'
    path = os.path.join("wind_analysis",
                        "wind_data",
                        csv_name)
    wind_df = pd.read_csv(path, index_col=0)
    wind_df.index = pd.to_datetime(wind_df.index)
    fig, ax = plt.subplots(3, 1, figsize=(5, 6), dpi=100)
    plot_on_axis(ax=ax[0],
                 data=wind_df['Apparent Temp(°C)'],
                 name=r'Temperature ($^{\circ}$C)',
                 c='firebrick')

    plot_on_axis(ax=ax[1],
                 data=wind_df['Wind(km/h)/(kt)'],
                 name='Wind Speed (kts)',
                 c='teal')

    plot_on_axis(ax=ax[2],
                 data=wind_df['WindDir.'].apply(compass_reversal.reverse),
                 name='Wind Direction',
                 c='mediumpurple',
                 xticks_wind=True,
                 compass_change=True,
                 rolling_window=5)
    _ = fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=5)

    windspeed = wind_df['Wind(km/h)/(kt)'][0]

    plot_arrow(compass_reversal.reverse(wind_df['WindDir.'][0]),
               row=1,
               column=3,
               image_path=os.path.join('wind_analysis',
                                       'images',
                                       'wind_arrow.png'),
               size=40 + 7*windspeed)

    plot_wind_text(time=wind_df.index[0],
                   temp=wind_df['Apparent Temp(°C)'][0],
                   speed=wind_df['Wind(km/h)/(kt)'][0],
                   direction=wind_df['WindDir.'][0],
                   gusts=wind_df['Gust(km/h)/(kt)'][0])
    plt.close(fig)


def plot_wind_text(time, temp, speed, direction, gusts):
    column = 3
    fontStyle = TkFont.Font(family="Lucida Grande", size=16)

    strtime = time.strftime("%a %H:%M")
    speed_label = tkinter.Label(
        root,
        text="Wind" + "\n" + str(speed) + ' knots ' + direction
                    + '\n' + 'gusts of ' + str(gusts) + ' kts',
        font=fontStyle)
    color = get_temp_colour(temp)
    temp_label = tkinter.Label(
        root,
        text='Temperature \n {:.1f}'.format(temp) + ' Deg C',
        font=fontStyle,
        background=color)

    date_label = tkinter.Label(
        root,
        text="Last Updated \n {}".format(strtime),
        font=fontStyle)

    speed_label.grid(row=0, column=column, pady=0, padx=1)
    temp_label.grid(row=2, column=column, pady=0, padx=1)
    date_label.grid(row=3, column=column, pady=0, padx=1)


# def _quit():
#     root.quit()     # stops mainloop
#     root.destroy()  # this is necessary on Windows to prevent
#                     # Fatal Python Error: PyEval_RestoreThread: NULL tstate


# button = tkinter.Button(master=root, text="Quit", command=_quit)
# button.pack(side=tkinter.BOTTOM)


# def update():
#     swell_data_main()
#     wind_location = 'Montague Island'
#     wind_data_url_dict = {'Montague Island': 'https://ozforecast.com.au/cgi-bin/weatherstation.cgi?station=94939',
#                           'Moruya Airport': "https://ozforecast.com.au/cgi-bin/weatherstation.cgi?station=95937"}
#     wind_data_main(wind_data_url_dict[wind_location])
#     place_swell_history()
#     plot_wind_history(wind_location)


# def add_update_button():
#     update_button = tkinter.Button(root, text="Update", command=update)
#     update_button.grid(row=5, column=1, columnspan=2, pady=1)


if __name__ == '__main__':
    swell_data_main()
    wind_location = 'Montague Island'
    wind_data_url_dict = {'Montague Island': 'https://ozforecast.com.au/cgi-bin/weatherstation.cgi?station=94939',
                          'Moruya Airport': "https://ozforecast.com.au/cgi-bin/weatherstation.cgi?station=95937"}
    wind_data_main(wind_data_url_dict[wind_location])
    root = tkinter.Tk()
    # add_update_button()

    root.title('Batemans Bay Surf Map')
    root.iconbitmap(os.path.join('images', 'surf-icon.ico'))
    place_swell_history()
    plot_wind_history(wind_location)
    root.mainloop()

# Global Imports
import tkinter as tk
import tkinter.font as TkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
from PIL import ImageTk
# Local Imports
from swell_analysis.swell_data_download import swell_data_main
from wind_analysis.wind_data_download import wind_data_main
from tools.compass import compass_reversal
from tools.color_converter import get_temp_colour
from tools.plotting import plot_on_axis, generate_arrow_image


class SwellDataDisplayer:
    def __init__(self, parent, *args, **kwargs):

        self.parent = parent
        self.frame = tk.Frame(self.parent)
        swell_data_main()
        # Call in csv data
        self.swell_height, self.swell_period, self.swell_direction = \
            self.get_and_clean_data()
        # Generate the canvases, images and buttons
        self.fig, self.ax = plt.subplots(3, 1, figsize=(5, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.update_button = tk.Button(self.frame,
                                       text="Update Swell Chart",
                                       command=self.update,
                                       height=2,
                                       width=20)
        self.place_swell_history()
        self.canvas.draw()
        self.arrowtk_image = ImageTk.PhotoImage(generate_arrow_image(
                angle=self.swell_direction[-1],
                size=40*self.swell_height[-1],
                image_path=os.path.join('swell_analysis',
                                        'images',
                                        'swell_arrow.png')))

        self.arrow_label = tk.Label(
            self.frame,
            image=self.arrowtk_image)
        self.arrow_label.image = self.arrowtk_image
        self.compass_direction, self.swell_label, self.date_format = \
            self.plot_swell_text(
                            time=self.swell_height.index[-1],
                            height=self.swell_height[-1],
                            period=self.swell_period[-1],
                            angle=self.swell_direction[-1])
        
        # Place all features
        self.update_button.grid(row=5, column=1, columnspan=2, pady=1)
        self.arrow_label.grid(row=1, column=0)
        self.date_format.grid(row=3, column=0, pady=0, padx=1)
        self.swell_label.grid(row=2, column=0, pady=0, padx=1)
        self.compass_direction.grid(row=0, column=0, pady=0, padx=1)
        self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=5)
        self.frame.pack(side=tk.LEFT)

    def get_and_clean_data(self):
        path = os.path.join("swell_analysis", "swell_data")
        data_fields = ['swell_height.csv',
                       'swell_period.csv',
                       'swell_direction.csv']
        swell_height = pd.read_csv(os.path.join(path, data_fields[0]))
        swell_period = pd.read_csv(os.path.join(path, data_fields[1]))
        swell_direction = pd.read_csv(os.path.join(path, data_fields[2]))
        swell_height = self.convert_to_datetime(swell_height).iloc[:, 1]
        swell_period = self.convert_to_datetime(swell_period).iloc[:, 0]
        swell_direction = self.convert_to_datetime(swell_direction).iloc[:, 0]
        return swell_height, swell_period, swell_direction

    def place_swell_history(self):

        plot_on_axis(ax=self.ax[0],
                     data=self.swell_height,
                     name='Swell Height (m)',
                     c='coral')

        plot_on_axis(ax=self.ax[1],
                     data=self.swell_period,
                     name='Swell Period (s)',
                     c='deepskyblue')

        plot_on_axis(ax=self.ax[2],
                     data=self.swell_direction,
                     name='Swell Direction',
                     c='palegreen',
                     xticks_swell=True,
                     compass_change=True)

        self.fig.tight_layout()
        plt.close(self.fig)

    def plot_swell_text(self, time, height,
                        period, angle):

        fontStyle = TkFont.Font(family="Lucida Grande", size=16)

        strtime = time.strftime("%a %H:%M")
        compass_direction = tk.Label(
            self.frame,
            text="Swell Direction" + \
                "\n" + compass_reversal[angle] + \
                " ({})".format(str(angle)),
            font=fontStyle)

        swell_label = tk.Label(
            self.frame,
            text="{:.2f} m \n @ {:.2f} seconds".format(height, period),
            font=fontStyle)

        date_format = tk.Label(
            self.frame,
            text="Last Updated \n {}".format(strtime),
            font=fontStyle)

        return compass_direction, swell_label, date_format

    def convert_to_datetime(self, df):
        df = df.set_index(
            pd.to_datetime(df.iloc[:, 0],
                        format="%Y-%m-%d %H:%M:%S"))
        df = df.iloc[:, 1:]
        return df

    def update(self):
        swell_data_main()
        self.arrow_label.grid_forget()
        self.date_format.grid_forget()
        self.swell_label.grid_forget()
        self.compass_direction.grid_forget()
        self.canvas.get_tk_widget().grid_forget()

        self.swell_height, self.swell_period, self.swell_direction = \
            self.get_and_clean_data()
        # Generate the canvases, images and buttons
        self.fig, self.ax = plt.subplots(3, 1, figsize=(5, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.place_swell_history()
        self.canvas.draw()
        self.arrowtk_image = ImageTk.PhotoImage(generate_arrow_image(
            angle=self.swell_direction[-1],
            size=40*self.swell_height[-1],
            image_path=os.path.join('swell_analysis',
                                    'images',
                                    'swell_arrow.png')))
        self.arrow_label = tk.Label(
            self.frame,
            image=self.arrowtk_image)
        self.compass_direction, self.swell_label, self.date_format = \
            self.plot_swell_text(
                            time=self.swell_height.index[-1],
                            height=self.swell_height[-1],
                            period=self.swell_period[-1],
                            angle=self.swell_direction[-1])

        self.arrow_label.grid(row=1, column=0)
        self.date_format.grid(row=3, column=0, pady=0, padx=1)
        self.swell_label.grid(row=2, column=0, pady=0, padx=1)
        self.update_button.grid(row=5, column=1, columnspan=2, pady=1)
        self.compass_direction.grid(row=0, column=0, pady=0, padx=1)
        self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=5)
        self.frame.pack(side=tk.LEFT)
        

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.swell_graphs = swell_graphs()
    

class WindDataDisplayer:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.data_location = tk.StringVar(self.frame)
        self.data_location.set("Moruya Airport")
        self.wind_data_url_dict = {
            'Montague Island': 'https://ozforecast.com.au/'
                               'cgi-bin/weatherstation.cgi?'
                               'station=94939',
            'Moruya Airport': 'https://ozforecast.com.au/'
                              'cgi-bin/weatherstation'
                              '.cgi?station=95937'}
        wind_data_main(self.wind_data_url_dict[self.data_location.get()])

        # Call in csv data
        self.wind_data = self.get_and_clean_data()
        
        # Generate Buttons and labels 
        self.fig, self.ax = plt.subplots(3, 1, figsize=(5, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.update_button = tk.Button(self.frame,
                                       text="Update Wind Chart",
                                       command=self.update,
                                       height=2,
                                       width=20)
        self.location_selector = tk.OptionMenu(
            self.frame,
            self.data_location,
            *list(self.wind_data_url_dict.keys()))
        self.place_wind_history()
        self.canvas.draw()
        self.arrowtk_image = ImageTk.PhotoImage(generate_arrow_image(
                angle=compass_reversal.reverse(self.wind_data['WindDir.'][0]),
                size=40 + 7*self.wind_data['Wind(km/h)/(kt)'][0],
                image_path=os.path.join('wind_analysis',
                                        'images',
                                        'wind_arrow.png')))
        self.arrow_label = tk.Label(
            self.frame,
            image=self.arrowtk_image)
        self.arrow_label.image = self.arrowtk_image
        self.speed_label, self.temp_label, self.date_label = \
            self.plot_wind_text(time=self.wind_data.index[0],
                                temp=self.wind_data['Apparent Temp(°C)'][0],
                                speed=self.wind_data['Wind(km/h)/(kt)'][0],
                                direction=self.wind_data['WindDir.'][0],
                                gusts=self.wind_data['Gust(km/h)/(kt)'][0])
        
        # Place all buttons on frame
        self.location_selector.grid(row=5, column=1, pady=1)
        self.update_button.grid(row=5, column=0, pady=1)
        self.arrow_label.grid(row=1, column=1)
        self.speed_label.grid(row=0, column=1, pady=0, padx=1)
        self.temp_label.grid(row=2, column=1, pady=0, padx=1)
        self.date_label.grid(row=3, column=1, pady=0, padx=1)
        self.canvas.get_tk_widget().grid(row=0, column=0, rowspan=5)
        self.frame.pack(side=tk.RIGHT)

    def get_and_clean_data(self):
        csv_name = self.data_location.get().replace(' ', '_') + '_Wind_Data.csv'
        path = os.path.join("wind_analysis",
                            "wind_data",
                            csv_name)    
        wind_df = pd.read_csv(path, index_col=0)
        wind_df.index = pd.to_datetime(wind_df.index)
        return wind_df

    def place_wind_history(self):

        plot_on_axis(ax=self.ax[0],
                     data=self.wind_data['Apparent Temp(°C)'],
                     name=r'Temperature ($^{\circ}$C)',
                     c='firebrick')

        plot_on_axis(ax=self.ax[1],
                     data=self.wind_data['Wind(km/h)/(kt)'],
                     name='Wind Speed (kts)',
                     c='teal')

        plot_on_axis(ax=self.ax[2],
                     data=self.wind_data['WindDir.']
                     .apply(compass_reversal.reverse),
                     name='Wind Direction',
                     c='mediumpurple',
                     xticks_wind=True,
                     compass_change=True,
                     rolling_window=5)

        _ = self.fig.tight_layout()
        plt.close(self.fig)

    def plot_wind_text(self, time, temp,
                       speed, direction,
                       gusts):

        fontStyle = TkFont.Font(family="Lucida Grande", size=16)

        strtime = time.strftime("%a %H:%M")
        speed_label = tk.Label(
            self.frame,
            text="Wind" + "\n" + str(speed) + ' knots ' + direction
                        + '\n' + 'gusts of ' + str(gusts) + ' kts',
            font=fontStyle)
        color = get_temp_colour(temp)
        temp_label = tk.Label(
            self.frame,
            text='Temperature \n {:.1f}'.format(temp) + ' Deg C',
            font=fontStyle,
            background=color)

        date_label = tk.Label(
            self.frame,
            text="Last Updated \n {}".format(strtime),
            font=fontStyle)

        return speed_label, temp_label, date_label

    def update(self):
        wind_data_main(self.wind_data_url_dict[self.data_location.get()])
        self.arrow_label.grid_forget()
        self.speed_label.grid_forget()
        self.temp_label.grid_forget()
        self.date_label.grid_forget()
        self.canvas.get_tk_widget().grid_forget()

        self.wind_data = self.get_and_clean_data()
        # Generate Buttons and Labels
        self.fig, self.ax = plt.subplots(3, 1, figsize=(5, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.update_button = tk.Button(self.frame,
                                       text="Update Wind Chart",
                                       command=self.update,
                                       height=2,
                                       width=20)
        self.place_wind_history()
        self.canvas.draw()
        self.arrowtk_image = ImageTk.PhotoImage(generate_arrow_image(
                angle=compass_reversal.reverse(self.wind_data['WindDir.'][0]),
                size=40 + 7*self.wind_data['Wind(km/h)/(kt)'][0],
                image_path=os.path.join('wind_analysis',
                                        'images',
                                        'wind_arrow.png')))
        self.arrow_label = tk.Label(
            self.frame,
            image=self.arrowtk_image)
        self.arrow_label.image = self.arrowtk_image
        self.speed_label, self.temp_label, self.date_label = \
            self.plot_wind_text(time=self.wind_data.index[0],
                                temp=self.wind_data['Apparent Temp(°C)'][0],
                                speed=self.wind_data['Wind(km/h)/(kt)'][0],
                                direction=self.wind_data['WindDir.'][0],
                                gusts=self.wind_data['Gust(km/h)/(kt)'][0])
        self.location_selector.grid(row=5, column=1, pady=1)
        self.update_button.grid(row=5, column=0, columnspan=1, pady=1)
        self.arrow_label.grid(row=1, column=1)
        self.speed_label.grid(row=0, column=1, pady=0, padx=1)
        self.temp_label.grid(row=2, column=1, pady=0, padx=1)
        self.date_label.grid(row=3, column=1, pady=0, padx=1)
        self.canvas.get_tk_widget().grid(row=0, column=0, rowspan=5)
        self.frame.pack(side=tk.RIGHT)





# def _quit():
#     root.quit()     # stops mainloop
#     root.destroy()  # this is necessary on Windows to prevent
#                     # Fatal Python Error: PyEval_RestoreThread: NULL tstate


# button = tkinter.Button(master=root, text="Quit", command=_quit)
# button.pack(side=tkinter.BOTTOM)





if __name__ == '__main__':
    root = tk.Tk()
    app1 = SwellDataDisplayer(root)
    app2 = WindDataDisplayer(root)
    root.mainloop()

    # swell_data_main()
    # wind_location = 'Montague Island'
    # wind_data_url_dict = {'Montague Island': 'https://ozforecast.com.au/cgi-bin/weatherstation.cgi?station=94939',
    #                       'Moruya Airport': "https://ozforecast.com.au/cgi-bin/weatherstation.cgi?station=95937"}
    # wind_data_main(wind_data_url_dict[wind_location])
    # root = tkinter.Tk()
    # # add_update_button()

    # root.title('Batemans Bay Surf Map')
    # root.iconbitmap(os.path.join('images', 'surf-icon.ico'))
    # place_swell_history()
    # plot_wind_history(wind_location)
    # root.mainloop()


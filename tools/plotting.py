from tkinter import image_names
from matplotlib.ticker import FormatStrFormatter
from matplotlib import dates
import matplotlib.ticker as mticker
import numpy as np
from tools.compass import compass_reversal
from PIL import Image


def plot_on_axis(ax, data, name, c,
                 xticks_swell=False,
                 xticks_wind=False,
                 compass_change=False,
                 rolling_window=3):

    data.rolling(window=rolling_window).mean().plot(
        ax=ax,
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
            ax.xaxis.set_tick_params(rotation=0)
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


def generate_arrow_image(angle, size, image_path):
    angle_calibrated = -90 - angle
    img = Image.open(image_path).rotate(angle_calibrated, expand=1).\
        resize((round(size), round(size)), Image.ANTIALIAS)
    return img


if __name__ == "__main__":
    path = 'swell_analysis\images\swell_arrow.png'
    img = generate_arrow_image(50, 100, path)
    img.show()
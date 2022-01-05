# A Live Surf Condition GUI
## Introduction
Over the holidays I have been actively surfing, and to avoid needing to drive excessively to get good quality waves, forecasting and exploring surf conditions is very important.
One of my largest frustrations is needing to go to many different websites in order to see live readings for swell, wind and tide. The program I have developed here scrapes all of the relevant information and places it in one tkinter GUI. The key python packages that were implemented in this project are:
 - BeautifulSoup - web scraping
 - tkinter - GUI building
 - PIL - image processing
 - matplotlib - plotting

I am currently extending its functionality to incorporate a wider range of locations.

## Data Sources
This project makes use of live swell data provided by [Manly Hydraulics Lab](https://mhl.nsw.gov.au/) as well as live wind data provided by [OzForecast](ozforecast.com.au)


## Usage
After installing the requirements.txt file, run *surfGUI.py*. The locations can be changed by selecting from the dropdowns and pressing *Update Swell/Wind Chart*.

### Example of GUI
![alt text](https://github.com/joshuamills98/LiveSurfGUI/blob/master/images/GUIscreenshot.png?raw=true)



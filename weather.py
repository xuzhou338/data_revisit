import requests, wget, os
from matplotlib import pyplot as plt, image as img
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as mpatches
import numpy as np
from datetime import datetime
import datetime as dt
from del_spines import del_spines
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'

class Weather():
    """This class tells you the current weather info and 5 day/ 3 hr forcast."""
    def __init__(self, zip=14623):
        """Store the zip code"""
        self.zip = zip
        self.icon = []

    def current_weather(self):
        """Show a short report of the current weather"""
        url = "http://api.openweathermap.org/data/2.5/weather?zip="
        url += str(self.zip) + "&APPID=e6c0c4b189f1bb754e65a35566372175"
        r = requests.get(url)
        api_response = r.json()

        # Read data from json
        current_weather = {}
        main = api_response['main']
        weather = api_response['weather'][0]
        wind = api_response['wind']
        self.icon = weather['icon']
        current_weather['name'] = api_response['name']
        current_weather['temperature'] = int(main['temp'] - 273.15)
        current_weather['condition'] = weather['main'] + " (" + \
                                    weather['description'] + ")"
        current_weather['humidity'] = main['humidity']
        current_weather['wind'] = str(wind['speed']) + " m/s"

        # Print the report
        for key in current_weather.keys():
            print(key.title() + ":", current_weather[key])

    def show_icon(self):
        """Show an icon of a current weather"""
        icon_url = "http://openweathermap.org/img/w/" + self.icon + ".png"
        icon_file = wget.download(icon_url)
        fig = plt.figure(1, (2,2))
        ax = del_spines(plt.gca())
        icon = img.imread(icon_file)
        ax.imshow(icon)
        os.remove(icon_file)
        plt.show()


    def five_day_graph(self):
        """Show five day weather forcast with both condition and temperature"""
        url = "http://api.openweathermap.org/data/2.5/forecast?zip=" + \
              str(self.zip) + "&APPID=e6c0c4b189f1bb754e65a35566372175"
        r = requests.get(url)
        response = r.json()

        time = []
        temp = []
        weather_5 = []
        city = response['city']
        data = response['list']

        # Adjust the time format
        for moment in data:
            time_txt = datetime.strptime(moment['dt_txt'], "%Y-%m-%d %H:%M:%S")
            time_new = datetime.strftime(time_txt, "%m-%d %I %p")
            time.append(time_new)
            temp.append(int(moment['main']['temp'] - 273.15))
            weather_5.append(moment['weather'][0]['main'])
        time_txt = time_txt + dt.timedelta(hours=3)
        time_new = datetime.strftime(time_txt, "%m-%d %I %p")
        time.append(time_new)

        major_time = [0]
        w_lines = [[0, None]]
        for i in range(40):
            if (i % 8) == 0 or i == 0:
                major_time.append(time[i])

            if i != 0 and i != len(weather_5) - 1:
                if weather_5[i] != weather_5[i - 1] and weather_5[i] != \
                        weather_5[i + 1]:
                    weather_5[i] = weather_5[i + 1]

                if weather_5[i] != weather_5[i-1]:
                    w_lines.append([i-1, weather_5[i-1]])
        w_lines.append([40, weather_5[-1]])
        major_time.append(time[-1])

        rain_color = [51/256, 153/256, 255/256]
        clouds_color = [230/256, 230/256, 230/256]

        plt.figure(1, (10, 5))
        ax = plt.axes(xlim=(0, 40))
        plt.plot(range(40), temp, c='pink')
        y_min, y_max = ax.get_ylim()
        ax.set_ylim(y_min, y_max)
        for i in range(len(w_lines)):
            if i > 0:
                w_code = {'Clear': 'orange', 'Rain': rain_color,
                          'Clouds': clouds_color}
                plt.fill_betweenx(np.arange(y_min, y_max+1), w_lines[i-1][0],
                                  w_lines[i][0], color=w_code[w_lines[i][1]],
                                  alpha=0.1)

        plt.xticks(range(40),major_time)
        ax = plt.gca()
        major_locator = MultipleLocator(8)
        minor_locator = MultipleLocator(1)
        ax.xaxis.set_major_locator(major_locator)
        ax.xaxis.set_minor_locator(minor_locator)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=-15, fontsize=10)
        plt.grid(axis='x', linestyle='--')
        plt.ylabel('Temperature (' + u'\N{DEGREE SIGN}' + 'C)')
        plt.title('5-Day Weather Forecast of ' + city['name'])
        clear_patch = mpatches.Patch(color='orange', alpha=0.1, label='Clear')
        rain_patch = mpatches.Patch(color=rain_color, alpha=0.1, label='Rain')
        clouds_patch = mpatches.Patch(color=clouds_color, alpha=0.1,
                                      label='Clouds')
        plt.legend(handles=[clear_patch, rain_patch, clouds_patch])
        plt.show()

if __name__ == "__main__":
    city_weather = Weather(14623)
    print("Current Weather:\n---------------------")
    city_weather.current_weather()
    #city_weather.show_icon()

    city_weather.five_day_graph()
import requests, wget, pygal, os
from matplotlib import pyplot as plt, image as img
from datetime import datetime

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
        icon = img.imread(icon_file)
        plt.imshow(icon)
        os.remove(icon_file)
        plt.show()

    def five_day_forecast(self):
        """Show five day weather forcast with both condition and temperature"""
        url = "http://api.openweathermap.org/data/2.5/forecast?zip=" + \
              str(self.zip) + "&APPID=e6c0c4b189f1bb754e65a35566372175"
        r = requests.get(url)
        response = r.json()

        time = []
        temp = []
        five_day_weather = []
        city = response['city']
        data = response['list']

        # Adjust the time format
        for moment in data:
            time_txt = datetime.strptime(moment['dt_txt'], "%Y-%m-%d %H:%M:%S")
            time_new = datetime.strftime(time_txt, "%m-%d %I %p")
            time.append(time_new)
            temp.append(int(moment['main']['temp'] - 273.15))
            five_day_weather.append(moment['weather'][0]['main'])

        # Print the report and shorten the time label for the plot below
        print("City Name: " + city['name'])
        for i in range(40):
            print(time[i] + " : " + five_day_weather[i])
            if (i % 4) != 0:
                time[i] = " "

        # Plot the temperature
        my_config = pygal.Config()
        my_config.x_label_rotation = 20
        my_config.label_font_size = 12
        line = pygal.Line(my_config)
        line.title = "Weather Forecast in Next 5 Days at " + city['name']
        line.x_labels = time
        line.add('Temperature', temp)
        line.render_in_browser()

if __name__ == "__main__":
    city_weather = Weather(14623)
    print("Current Weather:")
    city_weather.current_weather()
    city_weather.show_icon()
    print("-----------------------------")
    print("Five Day Forecast:")
    city_weather.five_day_forecast()
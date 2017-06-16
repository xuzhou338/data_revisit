import requests
import pygal
from datetime import datetime

url = "http://api.openweathermap.org/data/2.5/forecast?zip=14623&APPID=e6c0c4b189f1bb754e65a35566372175"
r = requests.get(url)
response = r.json()

city = response['city']
name = city['name']

data = response['list']
time = []
temp = []
weather = []


for moment in data:
    time_txt = datetime.strptime(moment['dt_txt'],"%Y-%m-%d %H:%M:%S")
    time_new = datetime.strftime(time_txt, "%m-%d %I %p")
    time.append(time_new)
    temp.append(int(moment['main']['temp'] - 273.15))
    weather.append(moment['weather'][0]['main'])

for i in range(40):
    print(time[i] + " : " + weather[i])
    if (i%4) != 0:
        time[i] = " "
my_config = pygal.Config()
my_config.x_label_rotation = 20
my_config.label_font_size = 12
line = pygal.Line(my_config)
line.title = "Weather Forecast in Next 5 Days at " + city['name']
line.x_labels = time
line.add('Temperature', temp)
line.render_in_browser()


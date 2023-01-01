import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Y7EQgy8RpQI')

soup = BeautifulSoup(page.content, 'html.parser')
seven_day =  soup.find(id='seven-day-forecast')
forecast_items = seven_day.find_all(class_='tombstone-container')
tonight = forecast_items[0]
# print(tonight.prettify())
period = tonight.find(class_='period-name').get_text()
desc = tonight.find(class_='short-desc').get_text()
temp = tonight.find(class_='temp').get_text()
img = tonight.find('img')
img_desc = img['title']

period_tags = seven_day.select('.tombstone-container .period-name')
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select('.tombstone-container .short-desc')]
temps = [t.get_text() for t in seven_day.select('.tombstone-container .temp')]
full_desc = [d['title'] for d in seven_day.select('.tombstone-container img')]


weather = pd.DataFrame({
    'period':periods,
    'short_desc':short_descs,
    'temp': temps,
    'desc': full_desc
})

# to pull out numberic temp values using regex and Series.str.extract
# temp_nums = weather["temp"].str.extract("(?Pd+)", expand=False)
# weather["temp_num"] = temp_nums.astype('int')

is_night = weather["temp"].str.contains('Low')
weather['is_night'] = is_night
print(weather)


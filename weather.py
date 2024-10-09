import pandas as pd
from bs4 import BeautifulSoup
import requests 
import html5lib
import re

#Request to the National Weather Service.
r =requests.get("https://forecast.weather.gov/MapClick.php?lat=28.2037609&lon=-82.2966151")
response = r.text

#Parse the data in HTML format.
soup = BeautifulSoup(response, "html.parser")

#Find the currentTemperature, Weather & Details.
temp = soup.find('p', class_="myforecast-current-lrg").text
weather = soup.find('div', id="current_conditions_detail").text
details = soup.find('div', class_= "col-sm-10 forecast-text" ).text

# Output to 3 separte file
with open("temp.txt", "w") as file:
        file.write(str(temp))
        file.close()

with open("weather.txt", "w") as file:
        file.write(str(weather))
        file.close()

with open("details.txt", "w") as file:
        file.write(str(details))
        file.close()

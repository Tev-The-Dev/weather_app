import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#creating an object of ToastNotifier class
n = ToastNotifier()

#define a function for getting data from the given url
def getdata(url):
    r = requests.get(url)
    return r.text

#storing url data into a variable and using the bs4 package to parse through the data.
htmldata = getdata("https://weather.com/weather/today/l/d2f1e335ae7b8adab5b01cf7aae6511ad388c9a90c0d9d566855282b6031c688")
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())

# Filter for the required data
current_temp = soup.find("span", class_="CurrentConditions--tempValue--zUBSz")  # Updated class name
chances_rain = soup.find("span", class_="Accessibility--visuallyHidden--n+vd9").next_sibling  # Updated class name

#Extracting the text from the found elements
temp = current_temp.text if current_temp else "N/A" #Get the first element's text
temp_rain = chances_rain.text if chances_rain else "N/A" #Get the first element's text

#prepare the result message
result = f"Current Temperature in Euless, TX: {temp}\nChance of rain: {temp_rain}"

#show the toast notification
n.show_toast("Weather update", result, duration = 10)
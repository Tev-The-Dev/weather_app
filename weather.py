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
htmldata = getdata("https://weather.com/en-US/weather/today/l/32.8371,-97.0814?par=google&temp=c/")
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())

#filter for the required data
current_temp = soup.find_all("span", class_="CurrentConditions--tempValue--3a50n")  # Update this class name
chances_rain = soup.find_all("div", class_="CurrentConditions--precipValue--2aJSf")  # Update this class name

#Extracting the text from the found elements
temp = current_temp[0].text if current_temp else "N/A" #Get the first element's text
temp_rain = chances_rain[0].text if chances_rain else "N/A" #Get the first element's text

#prepare the result message
result = f"Current Temperature in Euless, TX: {temp}\nChance  fo rain: {temp_rain}"

#show the toast notification
n.show_toast("Weather update", result, duration = 10)
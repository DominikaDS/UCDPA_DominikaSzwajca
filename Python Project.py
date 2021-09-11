#Importing data

##Retrieve data from online APIs
import request
import requests

data=requests.get('http://api.open-notify.org/iss-now.json')

print(data.text)

#mydata=data.json()
#print(mydata["message"])

dataDS=requests.get('http://api.open-notify.org/astros.json')

print(dataDS)

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=IUPMYGJCCYPZT908'
r = requests.get(url)
mydata = r.json()

print(mydata)

##Import a CSV file into a Pandas DataFrame
import pandas as pd

cars=pd.read_csv("norway_new_car_sales_by_make.csv")
print(cars.head())







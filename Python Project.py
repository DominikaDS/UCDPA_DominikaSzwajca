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

#List methods - sorting brands in ascending order
make=["Toyota", "Volkswagen", "Peugeot", "Ford", "Volvo"]
make.sort()
print(make)

#List methods - indexing
make=["Toyota", "Volkswagen", "Peugeot", "Ford", "Volvo"]
quantity = [2884, 2521, 1029, 870, 693]
make.index("Peugeot")
print(quantity[2])

#Grouping
grouped_pc = cars.groupby(["Make"]).mean()
print(grouped_pc)

#Drop duplicates
Duplicates=cars.drop_duplicates(subset=["Month"])
print(Duplicates)

#Looping
IrlTopBrand=["Toyota", "Volkswagen", "Hyundai"]
for p in IrlTopBrand:
    print(p)

#Iterrows
# Define a dictionary containing students data
data = {"Make": ["Toyota", "Volkswagen", "Peugeot", "Ford"],
                "Quantity":[2884, 2521, 1029, 870],
                "Pct":[22.7, 19.9, 8.1, 6.9],
                "Month":[1,1,1,1]}
df=pd.DataFrame(data, columns = ["Make","Quantity","Pct","Month"])
print("Top brand data:\n", df)
print("\nIterating over rows using loc function :\n")

# iterate through each row and select
# "Make" and "Quantity" column respectively
for i in range(len(df)) :
  print(df.loc[i, "Make"], df.loc[i, "Quantity"])


##Import a CSV file into a Pandas DataFrame
import pandas as pd

month=pd.read_csv("norway_new_car_sales_by_month.csv")
print(month.info())

#NumPy
import numpy as np
pivot=month.pivot_table(values="Quantity", index="Year",columns="Month",aggfunc=np.sum, margins=True, fill_value=0)
print(pivot)


#NumPy
import numpy as np
pivot1=cars.pivot_table(values="Quantity", index="Make",columns="Month",aggfunc=np.sum, margins=True, fill_value=0)
print(pivot1)

pivot2=cars.pivot_table(values="Quantity", index="Year",columns="Month",aggfunc=np.sum, margins=True, fill_value=0)
print(pivot2)


print(cars.head())

print(month.head())

print(pivot.head())

print(pivot1.head())

print(pivot2.head())



#Merge Data Frames

view=cars.agg({"Year": "count","Month": "count","Make": "count","Quantity": "mean"})
print(view)

view1=month.agg({"Year": "count","Month": "count","Import": "mean","Quantity": "mean"})
print(view1)


# merge both series
##df = pd.merge(a, b, "right_index"==True, "left_index"==True)

# show the dataframe
##print(df)




##result = pd.merge(view, view1["Import"],on="Year")
##print(result)


# Define a custom function to create reusable code
Short_VIN="XY123456"
Long_VIN="V12345678"
print("String 1:",Short_VIN)
print ("String 2:",Long_VIN)
Full_VIN=Long_VIN+Short_VIN
print("Concatenated chassis number:",Full_VIN)



# use of user defined functions

#Dictionary or Lists
##List

PCs_list=["108","208","308","508","2008","3008","5008","Traveller"]
print(PCs_list[1:])


##Dictionary

DS_regsYTD = {"DS3" : 7, "DS7" : 16, "NRDS" :5, "GODS" : 18}
DS_dealer=DS_regsYTD.get("NAVAN")
print(DS_dealer)


##Matplotlib

#Chart1

Matplot=pd.read_csv("Matplotdataset.csv")
print(Matplot.head())

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(Matplot["Country"], Matplot["Revenue"])
ax.set_xticklabels(Matplot["Country"], rotation=90)
ax.set_ylabel("Revenue")
plt.show()


#Chart 2
import seaborn as sns
sns.set_theme(style="whitegrid")
ax = sns.barplot(x="Continent", y="Revenue", data=Matplot, palette="Blues_d")
plt.show()




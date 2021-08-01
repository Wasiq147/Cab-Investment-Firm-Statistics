import pandas as pd

#This code is simply to extract all the information from all the files for use in other codes

transaction_data = pd.read_csv("Transaction_ID.csv", header=0)
TrID = transaction_data['Transaction ID'].tolist()
CuID = transaction_data['Customer ID'].tolist()
Payment = transaction_data['Payment_Mode'].tolist()

cab_data = pd.read_csv("Cab_Data.csv", header=0)
TID = cab_data['Transaction ID'].tolist()
DT = cab_data['Date of Travel'].tolist()
Com = cab_data['Company'].tolist()
City = cab_data['City'].tolist()
KM = cab_data['KM Travelled'].tolist()
Price = cab_data['Price Charged'].tolist()
Cost = cab_data['Cost of Trip'].tolist()

customer_data = pd.read_csv("Customer_ID.csv", header=0)
CID = customer_data['Customer ID'].tolist()
Gender = customer_data['Gender'].tolist()
Age = customer_data['Age'].tolist()
Income = customer_data['Income (USD/Month)'].tolist()

city_data = pd.read_csv("City.csv", header=0)
Cityy = city_data['City'].tolist()
Population = city_data['Population'].tolist()
Users = city_data['Users'].tolist()
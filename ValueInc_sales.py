import pandas as pd

data = pd.read_csv('transaction.csv', sep=';')

#Data Summary
data.info()

#Calculations 
#Defining Variables
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding new column to dataframe
data['CostPerTransaction'] = CostPerTransaction

#Sales per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Company's Profit
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Company Markup
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

#Rounding Markup
data['Markup'] = round(data['Markup'], 2)

#Combining Data Fields
data.head()


#Changing Column Type
print(data['Day'].dtype)
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)
my_date = day+'-'+data['Month']+'-'+year

data['Date'] = my_date

#Using iloc to view specific columns/rows
data.iloc[0:10] #First 10 Rows
data.iloc[-5:]   #Last 5 Rows

data.head(5)

data.iloc[4,2]  #Fourth Row Second Column

#Splitting the Client_Keywords field
split_col = data['ClientKeywords'].str.split(',' , expand=True)

#Creating new columns for the split columns
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#Removing Brackets and commmas from columns
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#Changing Items to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#Importing new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#Mergeing files
data = pd.merge(data, seasons, on = 'Month')

#Dropping Columns
data = data.drop('ClientKeywords', axis=1)
data = data.drop(['Day', 'Year', 'Month'], axis=1)

#Exporting to csv
data.to_csv('ValueInc_Cleaned.csv', index = False)
import pandas as pd

#  read data from a CSV file into a dataframe

# df=pd.read_csv('sample.csv', encoding='utf-8')
# print(df)


# creating a dataframe and saving into file

# data={
#     'Name':['sagar','alice','bob'],
#     'Age':[20,25,22],
#     'City':['butwal','kathmandu','bharatput']
# }

# df=pd.DataFrame(data)
# print(df)

# saving dataframe into file
# df.to_csv('output.csv',index=False) # CSV file
# df.to_excel('output.xlsx',index=False) # excel file
# df.to_json('output.json',index=False) # JSON file


# Exploring data: why?
# 1.understand the dataset
# 2.identify the problems
# 3.plan next steps


# head(n) and tail(n): if not n: 5 default

# df=pd.read_csv('sample.csv')
# print(df.head(7)) # first seven rows: index 0-6
# print(df.tail()) # last 5 rows

# info()-tells no of row and column,column name,dtype,non null counts,memory use of dataframe

# df=pd.read_csv('sample.csv')
# print('info of dataset:')
# print(df.info())


# describing dataframe

# data={'name':['ram','shyam','ghanshyam','dhanshyam','aditi','jagdish','raj','simran'],
#       'age':[10,20,30,40,50,60,25,32],
#       'salary':[50000,40000,45000,52000,49000,70000,48000,58000],
#       'performance score':[85,90,78,92,88,95,80,89]
#       }

# df=pd.DataFrame(data)
# print(df)
# print('descriptive statistics')
# print('\n',df.describe())

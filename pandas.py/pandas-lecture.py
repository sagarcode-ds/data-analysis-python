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


# shapes and columns
# how big is your dataset? (row,column)
# what are the names of columns?

# print('shape:',df.shape)
# print('column names:',df.columns)


# [] and boolean conditioning

# 1.select specific columns
# column=df['column name'] # 1 column
# column=df['column 1','column 2','column 3'] # ... column n


# for example
# name=df['name']
# print('name column:')
# print(name)

# subset=df[['name','salary']]
# print(subset)


# filter rows
# filtered_rows=df[df['column name']>5000]
# or
# for multiple conditions, df[condition1 & condition2]

# example: select rows where salary > 50000
# high_salary = df[(df['salary'] > 50000) & (df['age'] > 30)]
# print('\nHigh salary rows:')
# print(high_salary)




#  advanced pandas 


# data={'name':['ram','shyam','ghanshyam','dhanshyam','aditi','jagdish','raj','simran'],
#       'age':[10,20,30,40,50,60,25,32],
#       'salary':[50000,40000,45000,52000,49000,70000,48000,58000],
#       'performance score':[85,90,78,92,88,95,80,89]
#       }

# df=pd.DataFrame(data)
# print(df)

# modifying items in dataframe
# df['bonus']=df['salary']*0.1
# print(df)

# using insert method 
# df.insert(column no,column name,data)

# df.insert(0,'employee id',[10,20,30,40,50,60,70,80])
# print(df)



# updating values
# df.los[row index,column name] = new value
# df.loc used when modifying an specific item

# updating salary of ram
# df.loc[0,'salary'] = 55000
# print(df) # modified

# increasing all salary by 5 percent
# df['salary'] = df['salary'] * 1.05
# print('updated salary:')
# print(df)


data={'name':['ram','shyam','ghanshyam','dhanshyam','aditi','jagdish','raj','simran'],
      'age':[10,20,30,40,50,60,25,32],
      'salary':[50000,40000,45000,52000,49000,70000,48000,58000],
      'performance score':[85,90,78,92,88,95,80,89]
      }

df=pd.DataFrame(data)
print('original')
print(df)
print('\n')

# removing columns
# df.drop(columns=['column name'],inplace=True/False) 

df.drop(columns=['performance score','age'],inplace=True)
print('modified')
print(df)


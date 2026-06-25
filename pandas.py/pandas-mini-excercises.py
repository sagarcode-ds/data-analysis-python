# Dataset for All Problems
# Use this data — copy it once, and all 12 problems use it.

import pandas as pd

data = {
    'Name':       ['Sagar', 'Alice', 'Bob', 'Charlie', 'Diana',
                   'Evan',  'Fiona', 'George', 'Hina', 'Iqbal'],
    'Age':        [20, 25, 22, 30, 28, 35, 23, 32, 27, 29],
    'City':       ['Butwal', 'Kathmandu', 'Bharatpur', 'Pokhara', 'Butwal',
                   'Kathmandu', 'Bharatpur', 'Pokhara', 'Butwal', 'Kathmandu'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR',
                   'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary':     [30000, 55000, 40000, 70000, 45000,
                   80000, 38000, 65000, 52000, 48000],
    'Score':      [85, 90, 78, 92, 88, 95, 80, 89, 87, 83]
}

# Level 1 — Creating, Saving, Loading, Exploring

# Problem 1
# Create a DataFrame from the data above. Save it to employees.csv (no index).
# Then read it back from the CSV file.
# Print the first 4 rows and the last 3 rows.

# df = pd.DataFrame(data)
# df.to_csv('employees.csv',index=False)
# content=pd.read_csv('employees.csv')
# print(content)
# print(content.head(4))  
# print(content.tail(3)) 


# Problem 2
# From the CSV you just loaded, print all four of these in one script:

# Shape of the DataFrame
# Column names
# info() output
# describe() output

# print('Shape of the DataFrame:',content.shape)
# print('Column names:',content.columns)
# print(content.info())
# print('\n',content.describe())


# Problem 3
# Using the DataFrame:


# Print data types using dtypes (not info())
# Print unique value counts per column using nunique()
# Print how many employees are from each City using value_counts()

# What do you notice about which columns have few unique values vs many?


# print('data types of each columns')
# print(content.dtypes)
# print(content.nunique())
# print(content['City'].value_counts())



# Level 2 — Column Selection & Basic Filtering

# Problem 4
# Select only the Name and Salary columns from the DataFrame and display the result.
# Then select Name, Department, and Score — display that too.

result=df[['Name','Salary']]
print(result)

result2=df[['Name','Department','Score']]
print('\n',result2)


# Problem 5
# Filter and display only employees whose Salary is greater than 50,000.
# After filtering, answer: how many employees qualify?
# (Hint: .shape or len() can help)

filtered_rows=df[df['Salary']>50000]
print('\n',filtered_rows)
print(len(filtered_rows))



# Problem 6
# Filter employees who satisfy BOTH conditions:

# Department is 'IT'
# Score is greater than 80

# Display only their Name, Department, and Score.


filtered=df[(df['Department']=='IT') & (df['Score']>80)]


filtered2=filtered[['Name','Department','Score']]
print(filtered2)
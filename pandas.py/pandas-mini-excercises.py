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

df = pd.DataFrame(data)
df.to_csv('employees.csv',index=False)
content=pd.read_csv('employees.csv')
print(content)
print(content.head(4))  
print(content.tail(3)) 


# Problem 2
# From the CSV you just loaded, print all four of these in one script:

# Shape of the DataFrame
# Column names
# info() output
# describe() output

print('Shape of the DataFrame:',content.shape)
print('Column names:',content.columns)
print(content.info())
print('\n',content.describe())


# Problem 3
# Using the DataFrame:


# Print data types using dtypes (not info())
# Print unique value counts per column using nunique()
# Print how many employees are from each City using value_counts()

# What do you notice about which columns have few unique values vs many?


print('data types of each columns')
print(content.dtypes)
print(content.nunique())
print(content['City'].value_counts())



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



# Level 3 — OR, NOT, isin, between

# Problem 7
# Find all employees in either the 'HR' or 'Finance' department.
# Solve this two ways:


# Once using |
# Once using .isin()


# Confirm both give the same result.

filtered=df[(df['Department']=='HR') | (df['Department']=='Finance')]
print(filtered)

filtered2 = df[df['Department'].isin(['Finance', 'HR'])]
print('\n',filtered2)

print(filtered.equals(filtered2))  # same


# Problem 8
# Find all employees who are NOT from 'Butwal'.
# Display their Name and City only.

not_butwal=df[~(df['City']=='Butwal')]

name_city=not_butwal[['Name','City']]
print(name_city)

# Problem 9
# Find employees whose Salary is between 40,000 and 65,000 (inclusive).
# Use .between().
# How many employees fall in this range?


mid_salary=df[df['Salary'].between(40000,65000)]
print(mid_salary)
print(len(mid_salary))

# Level 4 — Index Operations & File Round-Trip

# Problem 10
# Take your DataFrame and:


# Set 'Name' as the index — print it
# Reset the index back to default integers — print it
# In your own words: what changed visually between step 1 and step 2?

df_indexed = df.set_index('Name')
print(df_indexed)

df_reset = df_indexed.reset_index()
print('\n')
print(df_reset)


# Problem 11
# Save the DataFrame to a JSON file (employees.json).
# Read it back using read_json.
# Use info() on both the original and the re-loaded version.
# Are the dtypes exactly the same? If not, which column changed and why do you think that happened?

df.to_json('employees.json')
content=pd.read_json('employees.json')
print(content)

df.info()
content.info()
print(df.dtypes.equals(content.dtypes)) 


# Level 5 — Combined Challenge

# Problem 12
# This one combines everything. Write a single filter expression (no intermediate variables except the final result) that returns employees who:

# Are in the 'IT' or 'Finance' department
# Have a Salary between 35,000 and 70,000 (inclusive)
# Are NOT from 'Kathmandu'

# From that filtered result, display only Name, Department, City, and Salary.
# Bonus (new method to look up): sort the final result by Salary from highest to lowest using sort_values()


result = (df[(df['Department'].isin(['IT', 'Finance'])) & 
             (df['Salary'] >= 35000) & 
             (df['Salary'] <= 70000) & 
             (df['City'] != 'Kathmandu')]
          [['Name', 'Department', 'City', 'Salary']]
          .sort_values('Salary', ascending=False))

print("Filtered result (IT/Finance, Salary 35K-70K, not Kathmandu, sorted by Salary desc):")
print(result)
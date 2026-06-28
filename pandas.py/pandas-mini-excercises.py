# Datasets for All Problems



import pandas as pd

employees = pd.DataFrame({
    'emp_id':     [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'name':       ['Sagar', 'Alice', 'Bob', 'Charlie', 'Diana',
                   'Evan',  'Fiona', 'George', 'Hina', 'Iqbal'],
    'dept':       ['IT', 'HR', 'IT', 'Finance', 'HR',
                   'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'city':       ['Butwal', 'Kathmandu', 'Bharatpur', 'Pokhara', 'Butwal',
                   'Kathmandu', 'Bharatpur', 'Pokhara', 'Butwal', 'Kathmandu'],
    'salary':     [30000, 55000, None, 70000, 45000,
                   80000, None,  65000, 52000, 48000],
    'score':      [85, 90, 78, None, 88, 95, 80, 89, None, 83],
    'experience': [1, 4, 2, 8, 5, 10, 2, 7, 4, 3]
})

projects = pd.DataFrame({
    'emp_id':  [101, 102, 103, 105, 107, 111, 112],
    'project': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Alpha', 'Epsilon', 'Zeta'],
    'budget':  [50000, 80000, 30000, 70000, 45000, 90000, 60000]
})

print(employees)
print('\n')

# Problem 1 — Add & Insert

# a) Add a 'bonus' column = 8% of salary.
# b) Add an 'annual_salary' column = salary × 12.
# c) Using insert(), add a 'level' column at position index 1 with values:
# ['Junior', 'Mid', 'Junior', 'Senior', 'Mid', 'Senior', 'Junior', 'Senior', 'Mid', 'Mid']
# d) Observation question: what values appear in the bonus and annual_salary columns
# for the rows where salary was None? Why?

# employees['bonus']=employees['salary']*0.08
# employees['annual_salary']=employees['salary']*12
# employees.insert(1,'level',['Junior', 'Mid', 'Junior', 'Senior', 'Mid', 'Senior', 'Junior', 'Senior', 'Mid', 'Mid'])
# print(employees)
# NaN appears as pandas converts None in a numeric column to NaN (Not a Number) internally.



# Problem 2 — Update & Rename

# a) Bob's (emp_id 103) salary was entered incorrectly. Update it to 42000 using loc.
# b) All Finance employees are getting a 12% raise.
# Update their salaries using conditional loc (one line, no loop).
# c) Rename the column 'experience' to 'years_exp' using rename().
# d) Drop the 'bonus' and 'annual_salary' columns — you'll recalculate them properly
# after handling NaN.

# employees.loc[employees['emp_id'] == 103, 'salary'] = 42000
# employees.loc[employees['dept']=='Finance','salary'] *= (1+0.12)
# employees.rename(columns={'experience':'years_exp'}, inplace=True)
# employees.drop(columns=['bonus','annual_salary'],inplace=True)
# print(employees)


# Problem 3 — Duplicates & Concat

# Add these duplicate rows, then clean them:

# extra = pd.DataFrame({
#     'emp_id':     [101, 108],
#     'name':       ['Sagar', 'George'],
#     'dept':       ['IT', 'HR'],
#     'city':       ['Butwal', 'Pokhara'],
#     'salary':     [30000, 65000],
#     'score':      [85, 89],
#     'years_exp':  [1, 7],
#     'level':      ['Junior', 'Senior']
# })

# a) Concatenate extra vertically with employees (use ignore_index=True).
# How many rows now?
# b) Drop duplicates based on emp_id only. How many rows remain?
# c) Try again with keep='last'. What changed compared to keep='first'?

# employees2=pd.concat([employees,extra],axis=0,ignore_index=True)
# print(employees2)
# print('no of rows:',len(employees2))
# employees=employees2.drop_duplicates(subset='emp_id')
# print(employees)  #  emp_id 101 and 108 are removed from last occurrence

# employees2=employees2.drop_duplicates(subset='emp_id',keep='last')
# print(employees2)  #  emp_id 101 and 108 are removed from first occurrence



# Problem 4 — Identify Missing Values
# (Work on the original employees DataFrame — with NaN still present.)
# a) Print the count of missing values per column.
# b) Print the percentage of missing values per column.
# (Hint: divide isnull().sum() by len(df), multiply by 100, round to 2 decimals)
# c) Print only the rows that contain at least one missing value.
# (Hint: df[df.isnull().any(axis=1)])



employees = pd.DataFrame({
    'emp_id':     [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'name':       ['Sagar', 'Alice', 'Bob', 'Charlie', 'Diana',
                   'Evan',  'Fiona', 'George', 'Hina', 'Iqbal'],
    'dept':       ['IT', 'HR', 'IT', 'Finance', 'HR',
                   'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'city':       ['Butwal', 'Kathmandu', 'Bharatpur', 'Pokhara', 'Butwal',
                   'Kathmandu', 'Bharatpur', 'Pokhara', 'Butwal', 'Kathmandu'],
    'salary':     [30000, 55000, None, 70000, 45000,
                   80000, None,  65000, 52000, 48000],
    'score':      [85, 90, 78, None, 88, 95, 80, 89, None, 83],
    'experience': [1, 4, 2, 8, 5, 10, 2, 7, 4, 3]
})



no_missingValues=employees.isnull().sum()
print(no_missingValues)
print(round(no_missingValues/len(employees) * 100, 2))
print(employees[employees.isnull().any(axis=1)])




# Problem 5 — Fix Missing Values
# a) Fill missing salary with the mean of the salary column.
# b) Fill missing score using linear interpolation.
# c) After both fills, confirm no NaN remain using isnull().sum().
# d) On a SEPARATE copy of the original employees DataFrame, use
# dropna(subset=['salary']) instead of filling. How many rows survive?
# How many did you lose?
# e) Which approach is better for this dataset — filling or dropping? State your reason in a comment.

original = employees.copy()

employees['salary'] = employees['salary'].fillna(employees['salary'].mean())
print(employees)

employees['score'] = employees['score'].interpolate(method='linear')
print(employees)
print(employees.isnull().sum()) # no NaN across all columns

dropped = original.dropna(subset=['salary'])
print(dropped)
print("Rows remaining:", len(dropped))      # 8
print("Rows lost:", len(original) - len(dropped))   # 2

# Filling is better for this dataset because:
# - With only 10 rows, losing 2 rows (20% of data) to dropna is a significant loss.
# - The 2 missing salary values are only 20% of the column — well within the
#   acceptable range for mean imputation.
# - Mean fill preserves all rows for downstream analysis.
# - Dropping would be preferred only if the missing data is not random,
#   or if the dataset were large enough to absorb the loss.
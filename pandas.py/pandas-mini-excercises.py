# import pandas as pd
# Challenge 1 — Build and Save:
# Create a DataFrame with 5 students: columns student_name, marks, grade (A/B/C). Save it as both a CSV and a JSON file. Then reload the CSV and print the first 3 rows using head()

# data={
#     'student name':['sagar','alice','bob','riya','priya'],
#     'marks':[84,72,69,76,88],
#     'grade':['A','B','C','B','A']}

# df=pd.DataFrame(data)
# print(df)
# df.to_csv('output.csv',index=False)
# df.to_json('output.json')
# print('\nfirst 3 rows')
# df_reloaded = pd.read_csv('output.csv')   # reload from disk
# print(df_reloaded.head(3))


# Challenge 2 — Explore it:

# After reloading that CSV, run info() and answer in comments:
# How many non-null entries are there?
# What is the dtype of marks? Of grade?

# df_reloaded = pd.read_csv('output.csv')
# df_reloaded.info() # all 5 are non-null, dtype of marks-int64,dtype of grade-str

# Challenge 3 — Describe:
# Add a gpa column (float values like 3.5, 2.8, etc.) to your DataFrame. Run describe() and note: what is the mean GPA? What is the 50th percentile (median)?

# df_reloaded['GPA']=[3.5,2.8,3.2,3.75,2.78]
# # print(df_reloaded)
# print(df_reloaded.describe()) # mean GPA-3.206,median-3.2


# Challenge 4 — index trap:
# Save your DataFrame to CSV without index=False. Then reload and print it. What extra column appears? How would you fix this when reading the file? (Hint: look up the index_col parameter of read_csv)

# df.to_csv('saved.csv')
# reloaded=pd.read_csv('saved.csv',index_col=0)
# print(reloaded)

#  Challenges Round 2

# Use this dataset for all challenges:

import pandas as pd
data = {
    'name':       ['ram', 'shyam', 'gita', 'sita', 'hari', 'maya'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance'],
    'age':        [25, 30, 22, 35, 28, 40],
    'salary':     [55000, 48000, 62000, 71000, 45000, 68000],
    'experience': [2, 5, 1, 10, 3, 12]
}

df = pd.DataFrame(data)


# Challenge 1 — shape and columns:
# Print the shape. Then print only the column names. Then using shape, print a sentence like:
# "This dataset has 6 rows and 5 columns." — but using the actual values from shape, not hardcoded numbers.

shape=df.shape
print('shape:',shape)
print('column names:', df.columns.tolist())
print(f"This dataset has {shape[0]} rows and {shape[1]} columns.")


# Challenge 2 — column selection:
# Select and print only the name and salary columns. Then check — is the result a DataFrame or a Series? Verify using type().

print('name and salary columns:')
result=df[['name','salary']]
print(result)
print(type(result)) # DataFrame


# Challenge 3 — single filter:
# Filter and print all employees whose salary is greater than or equal to 60000.

result3=df[df['salary']>=60000]
print("all employees whose salary is greater than or equal to 60000")
print(result3)

# Challenge 4 — multi-condition filter:
# Filter employees who are in the 'IT' department and have more than 1 year of experience.

print("\nemployees who are in the 'IT' department and have more than 1 year of experience.")
result3=df[(df['department']=='IT') & (df['experience']>1)]
print(result3)


# Challenge 5 — filter then select:
# Find all employees older than 27. From those results, display only their name, department, and salary columns.

result4=df[df['age']>27]
column=result4[['name','department','salary']]
print('name, department, and salary columns.')
print(column)


# Challenge 6 — think about it (no code needed):
# You run df['salary'] > 50000 on its own without wrapping it in df[]. What does it return, and why is that useful?

# we can inspect it directly to see which rows qualify
# we can pass it straight into df[...] as a filter mask
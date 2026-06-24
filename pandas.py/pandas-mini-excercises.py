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
import pandas as pd
#panda series
grades = pd.Series([88, 90, 80, 97, 99], index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
grades 
print(grades.mean())
print(grades.min())
print(grades.max())

#panda dataframe
data = {"Name": ['Alice', 'Bob', 'Charlie'],
         "age": [25, 30, 35],
         "city": ['New York', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
print(df)
print(df[['Name', 'age', 'city']])

print(df[df["city"] == "New York"])

df["age"] = df["age"] + 1
print(df)

df["senior"] = df["age"] > 30
print(df)

print(df.loc[0, :])
#df.loc[row, column]

print(df.loc[:, "Name"])

print(df.iloc[0, :])


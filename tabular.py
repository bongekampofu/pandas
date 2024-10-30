import pandas as pd

df= pd.read_csv("Titanic.csv")
print(df.tail(10) )
print(df.dtypes)

df["Pclass"].isin([2, 3])
age_sex = df[["Age", "Sex"]]
print(age_sex)

above_35 = df[df["Age"] > 35]
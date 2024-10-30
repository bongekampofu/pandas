import pandas as pd
import  matplotlib.pyplot as plt

df=pd.read_csv('Titanic.csv')
# 1. What is the number of non-null values in each column?
df_counts = df.count()
print("Number of non-null values in each column:\n", df_counts)

# 2. What is the number of male and female passengers?
df_sex_count = df['Sex'].value_counts()
print("Number of male and female passengers:\n", df_sex_count)

# 3. Count the number of passengers in each cabin class using groupby
df_class_count = df.groupby("Pclass")["Pclass"].count()
print("Count of passengers in each Pclass:\n", df_class_count)

# 4. Group by 'Pclass' and count the number of passengers in each class for plotting
df11 = df.groupby("Pclass").size().reset_index(name="Count")
print("\nPassenger count by Pclass:\n", df11)

#What is the average age of the Titanic passengers?
df2=df["Age"].mean()
print(df2)
#What is the median age and ticket fare price of the Titanic passengers?
df4= df[["Age", "Fare"]].median()
print(df4)
#aggregating statistics for given columns can be defined using the DataFrame.agg() method:
df5=df.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)
print(df5)
#What is the average age for male versus female Titanic passengers?
df8=df.groupby("Sex")["Age"].mean()
print("this is df6")
df6=df[["Sex", "Age"]].groupby("Sex").mean()
print(df6)
#calculate mean of numeric columns
df7=df.groupby("Sex").mean(numeric_only=True)
print(df7)
#only avg age by gender
df8=df.groupby("Sex")["Age"].mean()
print(df8)
#What is the mean ticket fare price for each of the sex and cabin class combinations?
df9=df.groupby(["Sex", "Pclass"])["Fare"].mean()
print(df9)
#What is the number of passengers in each of the cabin classes?
df10=df["Pclass"].value_counts()
#the value_counts is actually a groupby operation in combination with counting of the number of records within each group
print(df10)

# Group by 'Pclass' and count the number of passengers in each class
#df11 = df.groupby("Pclass", as_index=False)["Pclass"].count()
#print(df11)
#df11.plot(kind="bar")
#plt.show()

# Group by 'Pclass' and count the number of passengers in each class
df11 = df.groupby("Pclass").size().reset_index(name="Count")

print(df11)  # Check the structure of df11

# Plotting the bar chart
plt.bar(df11['Pclass'].values, df11['Count'].values, color='skyblue')
plt.xlabel('Pclass')
plt.ylabel('Number of Passengers')
plt.title('Count of Passengers by Pclass')
plt.show()
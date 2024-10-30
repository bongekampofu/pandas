import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("Titanic.csv")
#print(df.tail(10) )
#print(df.dtypes)

df["Pclass"].isin([2, 3])
class_23 = df[(df["Pclass"] == 2) | (df["Pclass"] == 3)]
print(class_23)
age_sex = df[["Age", "Sex"]]
#print(age_sex)

above_35 = df[df["Age"] > 35]

#age is not known
age_no_na = df[df["Age"].notna()]
print(age_no_na )

#names of passengers older than 35 years
adult_names = df.loc[df["Age"] > 35, "Name"]
print(adult_names)

#rows 10 till 25 and columns 3 to 5.
extract = df.iloc[9:25, 2:5]
print(extract)

above_35["Age"].plot()
plt.show()

#groupby gender
#df2 = df.groupby('Sex')['Fare'].mean() #this will give indexing error
df3 = df.groupby('Pclass', as_index=False)['Fare'].mean()
print("Get mean of the grouped data:\n", df3)


# Create a bar graph
df3.plot(kind="bar")
plt.title('Fare by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()

# Example check for df3 being a DataFrame and having data

pclass = df3.iloc[:, :1]  # First column as DataFrame
fare = df3.iloc[:, -1:]   # Last column as DataFrame
print(pclass)
print(fare)
#values removes indexing from pclass and fare
plt.bar(df3['Pclass'].values, df3['Fare'].values, color='skyblue')
plt.xlabel('Pclass')
plt.ylabel('Average Fare')
plt.title('Average Fare by Pclass')
plt.show()
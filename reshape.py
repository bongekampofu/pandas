import pandas as pd
#titanic data
titanic = pd.read_csv("Titanic.csv")
print(titanic.head())

#air quality data
air_quality = pd.read_csv("air_quality_long.csv", index_col="date.utc", parse_dates=True)
print(air_quality.head())

titanic.sort_values(by="Age").head()

#sort the Titanic data according to the cabin class and age in descending order.
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()

#LONG TO WIDE TABLE FORMAT
#filter no2 in parameter column
no2 = air_quality[air_quality["parameter"] == "no2"]
print(no2)

## use 2 measurements (head) for each location (groupby)
#The result is a subset no2_subset containing only two NO₂ measurements for each location, ordered by date
no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset)

#I want the values for the three stations as separate columns next to each other
print(no2_subset.pivot(columns="location", values="value"))

#ploting
no2.pivot(columns="location", values="value").plot()

#I want the mean concentrations for no2 and pm in each of the stations in table form
print(air_quality.pivot_table(values="value", index="location", columns="parameter", aggfunc="mean"))

#When interested in the row/column margins (subtotals) for each variable, set the margins parameter to True:
print(air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins=True,
))

#The same result can be derived by grouping on both parameter and location:
print(air_quality.groupby(["parameter", "location"])[["value"]].mean())

#WIDE TO LONG FORMAT
#convert the previous/last code - wide back to long
# a new index to the DataFrame with reset_index()
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()
print(no2_pivoted.head())

#I want to collect all air quality measurements in a single column (long format)
#The pandas.melt() method on a DataFrame converts the data table from wide format to long format
# The column headers become the variable names in a newly created column
no_2 = no2_pivoted.melt(id_vars="date.utc")
print(no_2.head())

#The parameters passed to pandas.melt() can be defined in more detail
no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)
no_2.head()


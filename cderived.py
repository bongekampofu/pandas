import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
df.head()

#I want to express the NO2concentration of the station in London in mg/m
df["london_mg_per_cubic"] = df["station_london"] * 1.882
print(df.head())

#I want to check the ratio of the values in Paris versus Antwerp and save the result in a new column.
df["ratio_paris_antwerp"] = (df["station_paris"] / df["station_antwerp"])
print(df.head())

#rename columns
df_renamed = df.rename(
    columns={
        "station_antwerp": "BETR801",
    }
)
print(df_renamed.head())

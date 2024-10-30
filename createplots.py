import pandas as pd
import matplotlib.pyplot as plt

#index_col defines the first (0th) column as index of the resulting DataFrame
# parse_dates converts the dates in the column to Timestamp objects
air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.plot()
plt.show()

#plot only the columns of the data table with the data from Paris.
air_quality["station_paris"].plot()
plt.show()

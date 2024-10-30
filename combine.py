iimport pandas as pd
airquality2 = pd.read_csv("air_quality_no2_long.csv",
  parse_dates=True)

airquality2 = airquality2[["date.utc", "location",
       "parameter", "value"]]

airquality2.head()

pm25 = pd.read_csv("air_quality_pm25_long.csv",
                               parse_dates=True)

pm25 = pm25[["date.utc", "location",
                                     "parameter", "value"]]
pm25.head()

#combine the measurements of 2 tables with a similar structure, in a single table.

airquality = pd.concat([pm25, airquality2], axis=0)

print(airquality.head())
print(airquality["parameter"])

print('Shape of the ``air_quality_pm25`` table: ', pm25.shape)


print('Shape of the ``air_quality_no2`` table: ', airquality2.shape)


print('Shape of the resulting ``air_quality`` table: ', airquality.shape)

airquality = airquality.sort_values("date.utc")

airquality.head()

airquality = pd.concat([pm25, airquality2], keys=["PM25", "NO2"])

print(airquality.head())
print(airquality.tail())


#Join tables using a common identifier

#Add the station coordinates, provided by the stations metadata #table, to the corresponding rows in the measurements table

stations_coord = pd.read_csv("air_quality_stations.csv")

stations_coord.head()

airquality = pd.merge(airquality, stations_coord, how="left", on="location")

print(airquality.head())


#Add the parameters’ full description and name, provided by the #parameters metadata table, to the measurements table.

parameters = pd.read_csv("air_quality_parameters.csv")

parameters.head()

airquality = pd.merge(airquality, parameters,
   how='left', left_on='parameter', right_on='id')

airquality.head()



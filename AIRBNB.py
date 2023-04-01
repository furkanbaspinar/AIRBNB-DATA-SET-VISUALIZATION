
# This data set contains the listings and prices of Airbnb apartments in New York City.
# First of all, the data set needs to be loaded and cleaned.
# Given the size of the dataset, I will show only a few examples of visualization here.

# In the first example, we will visualize the distribution of Airbnb apartments located in Manhattan. We will use the geopandas library for this.
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Loading the data set
airbnb_df = pd.read_csv(r"C:\Users\furka\Desktop\AB_NYC_2019.csv")

# Merging columns containing coordinate data
airbnb_df['coordinates'] = list(zip(airbnb_df.longitude, airbnb_df.latitude))

# Converting geopandas to a data frame
airbnb_gdf = gpd.GeoDataFrame(airbnb_df,
                              geometry=gpd.points_from_xy(airbnb_df.longitude, airbnb_df.latitude))
# Load the Manhattan borders
nyc = gpd.read_file(gpd.datasets.get_path('nybb')).to_crs(epsg=4326)
manhattan = nyc[nyc['BoroName'] == 'Manhattan']

# Get only Manhattan locations in airbnb data
airbnb_manhattan = gpd.sjoin(airbnb_gdf, manhattan, op='within')
# Visualization!
fig, ax = plt.subplots(figsize=(12,10))
manhattan.plot(ax=ax, alpha=0.4, color='grey')
airbnb_manhattan.plot(ax=ax, markersize=1, color='blue', alpha=0.4)
plt.title('Distribution of Manhattan Airbnb apartments')
plt.show(block=True)

###################
# 2. Visualization
###################

# This code visualizes the distribution of Airbnb apartments located in Manhattan.
# The output shows a map of Manhattan in gray and the locations of Airbnb apartments in blue dots.
# In a second example, we will visualize a histogram showing the distribution of prices for Airbnb apartments in Manhattan.
import pandas as pd
import matplotlib.pyplot as plt

# Loading the data set
airbnb_df = pd.read_csv(r"C:\Users\furka\Desktop\AB_NYC_2019.csv")

# Selecting data only in Manhattan
airbnb_manhattan = airbnb_df[airbnb_df['neighbourhood_group'] == 'Manhattan']

# Visualization!!
plt.figure(figsize=(10,6))
plt.hist(airbnb_manhattan['price'], bins=50, range=(0,1000), alpha=0.5, color='blue')
plt.title('The Price Distribution of Airbnb Apartments')
plt.show()




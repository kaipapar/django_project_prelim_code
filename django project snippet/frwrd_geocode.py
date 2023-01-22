'''create another dataframe for long and lat coordinates of locations'''

#first pip install geopy and geopandas
import geopy
import geopandas as gpd
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import folium
from folium.plugins import FastMarkerCluster
import numpy as np
#from loc_from_txt import 

#how to geocode areas which do not have distinct coordinates.

locator =Nominatim(user_agent='myGeocoder')
location =locator.geocode('london')
print(location.address)
print(f'Latitude={location.latitude}, Longitude={location.longitude}')


'''geocode=RateLimiter(locator.geocode, min_delay_seconds=1)
location1='london'
geocoder=location1.apply(geocode)

#creating another dataframe where there are the coordinates for the locations in the original dataframe.

#making a df filled with zeros
df_zeros=pd.DataFrame(np.zeros((5,6)))

#doing operations on all 
for i in pd.iloc[df_zeros]:
    if i<=len(df_zeros)-1:

'''

# pd.iloc[]
# df[df.columns[2]]

#df[df.columns[x]]


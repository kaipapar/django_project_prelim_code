'''geocoding locations inside a dictionary'''

#questions
#how do I geocode an area which does not have distinct coordinates, but only boundaries?

import numpy as np
import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

    #big ass dictionary for complicated shizzle
loc_dict={'cities': ['Mumbai', 'Delhi', 'London', 'Munich', 'Haryana'], 'countries': ['India', 'Bangladesh', 'Pakistan'], 
'regions': ['Maharashtra', 'Haryana', 'Kerala', 'Nagaland'], 'other countries': ['India', 'United Kingdom', 'United States' , 'Canada', 'Germany', 'South Africa'], 'region cities': {'Maharashtra': ['Mumbai'], 'NCT': ['Delhi'], 'England': ['London' ], 'Texas': ['London'], 'New York': ['Delhi'], 'Ohio': ['London'], 'Louisiana': ['Delhi'], 'Ontario': ['London', 'Delhi'], 
'Kentucky': ['London'], 'Bavaria': ['Munich'], 'Mpumalanga': ['London'], 'California': ['Delhi'], 'Haryana': ['Haryana'], 'Iowa': ['Delhi'], 'Arkansas': ['London'], 'North Dakota': ['Munich']}, 'other regions': ['Maharashtra', 'NCT', 'England', 'Texas', 'New York', 'Ohio', 'Louisiana', 'Ontario', 'Kentucky', 'Bavaria', 'Mpumalanga', 'California', 'Haryana', 'Iowa', 'aArkansas', 'North Dakota'], 'other': []}

    #smaller dictionary for easier shizzle
smll_dict={'cities': ['Mumbai', 'Delhi', 'London', 'Munich', 'Haryana'], 'countries': ['India', 'Bangladesh', 'Pakistan']}

    #seeing all values in a dictionary
i=1
for value in smll_dict.values():
    print(value)
    print(i)
    i+=1


###unsure if this works
    #defining a copy of the dictionary where the coordinates are to be placed
loc_geoc=smll_dict
    #using nominatim  for geocoding
locator=Nominatim(user_agent='myGeocoder')
    #iterating through all values inside a dictionary:
for value in loc_geoc.values():
        #if the value is a list and it contains something:
    if type(value)==list and value!=None:
            #'i' should refer to an element in the list called value:
        for i in value:
            location=locator.geocode(i)
                #redefining the element i as a tuple containing coordinates:
            i=tuple((location.latitude, location.longitude))
            print(i)
        #if the value isn't a list:
    elif type(value)!=list:
        print('what are you?')
        #if the value is neither of the above requirements:
    else:
            print('value is unreachable')

    print(loc_geoc)

        #if I wanted to use the full dictionary this is what i would have to do.
    '''elif type(value)==dict and value != None:
        z='since it is a' '''

'''getting location-words from a string or txt file'''

#run req_locations from text.py first
'''import locationtagger as loc
import pandas as pd'''
from loc_from_txt import *
 
# initializing sample text
sample_text = "India has very rich and vivid culture widely spread from Kerala to Nagaland to Haryana to Maharashtra. Delhi being capital with Mumbai financial capital. Can be said better than some western cities such as Munich, London etc. Pakistan and Bangladesh share its borders"
#sample txt from path

#

#a big dictionary from the above text
loc_dict={'cities': ['Mumbai', 'Delhi', 'London', 'Munich', 'Haryana'], 'countries': ['India', 'Bangladesh', 'Pakistan'], 
'regions': ['Maharashtra', 'Haryana', 'Kerala', 'Nagaland'], 'other countries': ['India', 'United Kingdom', 'United States' , 'Canada', 'Germany', 'South Africa'], 'region cities': {'Maharashtra': ['Mumbai'], 'NCT': ['Delhi'], 'England': ['London' ], 'Texas': ['London'], 'New York': ['Delhi'], 'Ohio': ['London'], 'Louisiana': ['Delhi'], 'Ontario': ['London', 'Delhi'], 
'Kentucky': ['London'], 'Bavaria': ['Munich'], 'Mpumalanga': ['London'], 'California': ['Delhi'], 'Haryana': ['Haryana'], 'Iowa': ['Delhi'], 'Arkansas': ['London'], 'North Dakota': ['Munich']}, 'other regions': ['Maharashtra', 'NCT', 'England', 'Texas', 'New York', 'Ohio', 'Louisiana', 'Ontario', 'Kentucky', 'Bavaria', 'Mpumalanga', 'California', 'Haryana', 'Iowa', 'aArkansas', 'North Dakota'], 'other': []}

#print(f'cities {l_cities} \n countries {l_countries} \n regions {l_regions} \n other countries {l_other_countries} \n region cities {l_region_cities} \n other regions {l_other_regions} \n other {l_other} \n loc dict {loc_dict}')


print(parsed_locs_into_df(sample_text))
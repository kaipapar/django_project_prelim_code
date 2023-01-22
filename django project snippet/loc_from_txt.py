'''
FUNCTIONS FOR GETTING LOCATIONS FROM TEXTS

'''

#run req_locations from text.py first
import locationtagger as loc
import pandas as pd
import os
 
# initializing sample text
sample_text = "India has very rich and vivid culture widely spread from Kerala to Nagaland to Haryana to Maharashtra. Delhi being capital with Mumbai financial capital. Can be said better than some western cities such as Munich, London etc. Pakistan and Bangladesh share its borders"

#parsing locations from a text file and creating a place entity for it.
def loc_parse_from_file(file_path):
    if not os.path.isfile(file_path):
        return print('path not found')
    else:
        text=open(file_path, 'r')
        data=text.read()
        return loc.find_locations(text=data)

#parsing locations from a string variable
def parsed_locs_into_df(textvar):
    #getting the place entity for the variables
    place_entity=loc.find_locations(text=textvar)
    
    #defining list and dict variables per different criteria
    l_cities=place_entity.cities
    l_countries=place_entity.countries
    l_regions=place_entity.regions
    l_other_countries=place_entity.other_countries
    l_region_cities=place_entity.region_cities
    l_other_regions=place_entity.other_regions
    l_other=place_entity.other

    #defining the above list and dict variables as a dictionary
    loc_dict={'cities':l_cities,
    'countries':l_countries,
    'regions':l_regions,
    'other countries':l_other_countries,
    'region cities':l_region_cities,
    'other regions':l_other_regions,
    'other':l_other
    }

    '''
    #creating null values for empty places in the lists --> making all of the dictionary values the same lenght
    lmax = 0
    for lname in loc_dict.keys():
        lmax = max(lmax, len(loc_dict[lname]))
    for lname in loc_dict.keys():
        ll = len(loc_dict[lname])
        if  ll < lmax:
            loc_dict[lname] += ['null'] * (lmax - ll)'''
    
    #creating a dataframe from the dictionary
    loc_df=pd.DataFrame.from_dict(loc_dict,orient='index')
    '''
    #transposing the df
    loc_df=loc_df.transpose()'''
    return print(loc_df)
    
    #getting a dataframe with locations from a txt file
    #works
def parsed_locs_into_df_from_txt(path):
    text=open(path, 'r')
    data=text.read()
    place_entity=loc.find_locations(text=data)

    l_cities=place_entity.cities
    l_countries=place_entity.countries
    l_regions=place_entity.regions
    l_other_countries=place_entity.other_countries
    l_region_cities=place_entity.region_cities
    l_other_regions=place_entity.other_regions
    l_other=place_entity.other

    loc_dict={'cities':l_cities,
        'countries':l_countries,
        'regions':l_regions,
        'other countries':l_other_countries,
        'region cities':l_region_cities,
        'other regions':l_other_regions,
        'other':l_other
        }
    
    '''
    #giving null values for the locations in the df which do not have anything in them
    lmax = 0
    for lname in loc_dict.keys():
        lmax = max(lmax, len(loc_dict[lname]))
    for lname in loc_dict.keys():
        ll = len(loc_dict[lname])
        if  ll < lmax:
            loc_dict[lname] += ['null'] * (lmax - ll)'''
    
    loc_df=pd.DataFrame.from_dict(loc_dict,orient='index')
    '''
    #transposing the dataframe
    loc_df=loc_df.transpose()'''

    return loc_df



    #getting a big dict with locations from a txt file
    #works
def parsed_locs_into_dict_from_txt_big(path):
    text=open(path, 'r')
    data=text.read()
    place_entity=loc.find_locations(text=data)

    l_cities=place_entity.cities
    l_countries=place_entity.countries
    l_regions=place_entity.regions
    l_other_countries=place_entity.other_countries
    l_region_cities=place_entity.region_cities
    l_other_regions=place_entity.other_regions
    l_other=place_entity.other

    loc_dict={'cities':l_cities,
        'countries':l_countries,
        'regions':l_regions,
        'other countries':l_other_countries,
        'region cities':l_region_cities,
        'other regions':l_other_regions,
        'other':l_other
        }

    return loc_dict


    #getting a small(easier...) dict with locations from a txt file
    #works
def parsed_locs_into_dict_from_txt_smll(path):
    text=open(path, 'r')
    data=text.read()
    place_entity=loc.find_locations(text=data)

    l_cities=place_entity.cities
    l_countries=place_entity.countries

    loc_dict={'cities':l_cities,
        'countries':l_countries,
        }

    return loc_dict

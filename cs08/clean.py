import pandas as pd
import string
import re

city_name_map = {
    'Buirnsville': 'Burnsville',
    'Connelly': 'Connelly Springs',
    'Connelly Spring': 'Connelly Springs',
    'Connellys Springs': 'Connelly Springs',
    'Foresst City': 'Forest City',
    'Forest City, Nc 28043': 'Forest City',
    'Green Mtn': 'Green Mountain',
    'Green Mtn.': 'Green Mountain',
    'Henrrietta': 'Henrietta',
    'Mc Grady': 'McGrady',
    'Mcgrady': 'McGrady',
    'Mill Springs': 'Mill Spring',
    'Miller\'s Creek': 'Millers Creek',
    'Mooesboro': 'Mooresboro',
    'Moravianfalls': 'Moravian Falls',
    'Morgnton': 'Morganton',
    'Mroganton': 'Morganton',
    'N Wilkesboro': 'North Wilkesboro',
    'N. Wilkesboro': 'North Wilkesboro',
    'N.wilkesboro': 'North Wilkesboro',
    'North Wilesboro': 'North Wilkesboro',
    'North Wilkesbor': 'North Wilkesboro',
    'Noth Wilkesboro': 'North Wilkesboro',
    'Piney Crek': 'Piney Creek',
    'Robbinville': 'Robbinsville',
    'Ruthefordton': 'Rutherfordton',
    'Rutherford': 'Rutherfordton',
    'Wests Jefferson': 'West Jefferson',
    'Wilkeboro': 'Wilkesboro',
    'Wilkesboro, Nc 28697': 'Wilkesboro',
    'Wilkesboro28': 'Wilkesboro',
}

state_map = {
    'NC': 'NC',
    'Nc': 'NC',
    'nc': 'NC',
    'No': 'NC',
    'VA': 'VA',
    'Va': 'VA',
    'va': 'VA',
    'GA': 'GA',
    'Ga': 'GA',
    'ga': 'GA',
    'SC': 'SC',
    'Sc': 'SC',
    'sc': 'SC',
}

def clean_city(city):
    
    if (isinstance(city, str)):
        city = city.strip()                 #7
        city = re.sub(r'\s+', ' ', city)    #8
        city = city.title()                 #9
        city = re.split(',',city)[0]        #10
        if (city.endswith(' Nc')):          #11
            city = city[:-3]
        if (city in city_name_map):         #12
            city = city_name_map.get(city)

    return city

def clean_state(state):
    
    if (state in state_map):
        state = state_map.get(state)
    
    return state

def clean_zip(zip):
    
    if (isinstance(zip, str)):
        s = ''.join(filter(lambda i: i.isdigit(), zip))
        s = s[:5]
        if len(s)==5:
            return s
        
    return float('nan')

def main():

    df = pd.read_csv('basic_person.csv', index_col='acct_id_new')
    
    df['city'] = df['city'].apply(clean_city)
    df['state'] = df['state'].apply(clean_state)
    df['zip'] = df['zip'].apply(clean_zip)

    # print(df.groupby(by='state').count())
    
    df.to_csv('cleaned.csv')

    # df = pd.read_csv('cleaned.csv')
    # print(df.loc[12041:12060])
    



if __name__ == '__main__':
    main()
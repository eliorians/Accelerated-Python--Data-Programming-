
import pandas as pd


#oriansed = Pumpkin, Seminole

items = [    
    'Apples, Early Yellow Transparent',
    'Apples, Gala',
    'Apples, Gold Rush',

    'Apples, Red Rome Beauty',
    'Apples, Spice',
    'Basil, Fresh - Sweet Genovese (green)',

    'Beets, Without Greens',
    'Collards',
    'Garlic Scapes',
    'Jerusalem Artichokes',

    'Lettuce, Head',
    'Lettuce, Loose Leaf Green',
    'Microgreens, Sunshine Mix',

    'Okra, Green',
    'Peppers, Bell (Green)',
    'Peppers, Jalapeno',

    'Pumpkin, Seminole',
    'Rosemary, Fresh',
    'Sweet Potatoes, Orange',
    'Watermelon, Jubilee'
]


def myhash(user_name):
    import hashlib
    m = hashlib.sha256()
    m.update(bytes(user_name, 'utf-8'))
    return int(m.hexdigest()[:16], 16)

user_name = 'oriansed'
item = items[myhash(user_name)%len(items)]


unit_map = {
    '3 - 5 lbs.'   : '1 lb',
    '6 - 9 lbs.'   : '1 lb',
    '10 - 15 lbs.' : '1 lb',
}

def clean_unit(unit):
    if (unit in unit_map):
        unit = unit_map.get(unit)

    return unit

def clean(row):
    
    if row['SubCategory'] == 'Pumpkin, Seminole':
        if row['Unit'] == '3 - 5 lbs.':
            row['Units Sold'] = row['Units Sold'] * 4
        if row['Unit'] == '6 - 9 lbs.':
            row['Units Sold'] = row['Units Sold'] * 7.5
        if row['Unit'] == '10 - 15 lbs.':
            row['Units Sold'] = row['Units Sold'] * 12.5
        row['Unit'] = clean_unit(row['Unit'])
    
    return row


def main():
    
    #load
    df = pd.read_csv('food.csv')

    #clean
    df = df.apply(lambda x: clean(x), axis = 1)

    #save
    df.to_csv('cleaned_produce.csv')

if __name__ == '__main__':
    main()
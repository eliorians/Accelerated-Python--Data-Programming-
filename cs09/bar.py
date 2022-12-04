
import pandas as pd
import matplotlib.pyplot as plt

og_dates = ['19-Jan', '19-Feb', '19-Mar', '19-Apr', '19-May', '19-Jun', '19-Jul', '19-Aug', '19-Sep', '19-Oct', '19-Nov', '19-Dec']

new_dates = {'19-Jan': 'Jan','19-Feb': 'Feb','19-Mar': 'Mar', '19-Apr': 'Apr', '19-May': 'May','19-Jun': 'Jun','19-Jul': 'Jul','19-Aug': 'Aug','19-Sep': 'Sep','19-Oct': 'Oct','19-Nov': 'Nov','19-Dec': 'Dec'}

month_dict = {'Jan':1,'Feb':2,'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}


def clean_date(date):
    if (date in new_dates):
        date = new_dates.get(date)
    
    return date

def main():
    #load files / get input
    cat = input("Enter SubCategory: ")
    df = pd.read_csv('food_cleaned.csv')

    #reduce to rows we want
    df = df.loc[df['SubCategory'] == cat]
    df = df.loc[df['Month Sold'].isin(og_dates)]
    unit = df['Unit'].iat[0] + "s of "

    #aggregate by month
    df = df.groupby('Month Sold', as_index=False).sum()
    
    #sort dates
    df['Month Sold'] = df['Month Sold'].apply(clean_date)
    df = df.sort_values('Month Sold', key = lambda x : x.apply (lambda x : month_dict[x]))

    #create axis lists
    x = df['Month Sold'].tolist()
    y = df['Units Sold'].tolist()

    #graph
    plt.bar(x, y)
    plt.title(unit + cat)
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.show()
    

if __name__ == '__main__':
    main()


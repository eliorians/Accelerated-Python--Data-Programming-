
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
    startswith = input("Keep subcategories that start with: ")
    df = pd.read_csv('food_cleaned.csv')

    #reduce df to only SubCategories that begin the same as startswith
    df = df.loc[df['SubCategory'].str.startswith(startswith)]
    #reduce to only 2019
    df = df.loc[df['Month Sold'].isin(og_dates)]

    #split into multiple dfs
    #https://stackoverflow.com/questions/19790790/splitting-dataframe-into-multiple-dataframes
    uniqueCats = df.SubCategory.unique()
    dfDic = {elem : pd.DataFrame() for elem in uniqueCats}
    for key in dfDic.keys():
        dfDic[key] = df[:][df.SubCategory == key]
    
    #order and group data
    for i in uniqueCats:
        df = dfDic[i]

        #aggregate each df sales by months
        dfDic[i] = df.groupby('Month Sold', as_index=False).sum()
        
        #order months
        df['Month Sold'] = df['Month Sold'].apply(clean_date)
        df = df.sort_values('Month Sold', key = lambda x : x.apply (lambda x : month_dict[x]))


    #sub plots
    #https://www.appsloveworld.com/pandas/100/157/how-to-plot-a-dictionary-of-dataframes-to-subplots
    fig, axes = plt.subplots(nrows = len(dfDic), ncols = 1)
    
    #initialize colors
    colors = plt.rcParams["axes.prop_cycle"]()
    
    for i, key in enumerate(dfDic):
        df = dfDic[key]
        c = next(colors)["color"]
        
        df.plot.bar(ax=axes[i], title=key, legend=None, x='Month Sold', y='Units Sold', rot=0, color=c)#.axis('off')
        

    
    plt.subplots_adjust(hspace=.7)
    plt.show()

if __name__ == '__main__':
    main()
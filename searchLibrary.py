import os
import pandas as pd
import utilities
import numpy as np
from app import artworkSet,countrySet

#filter1
class stats():
    def __init__(self,df1):
        self.df = df1
        self.temp = ''
    def topTen(self,cat):
        temp = pd.pivot_table(self.df,index = cat, aggfunc = 'count')
        temp = temp.to_records()
        temp = pd.DataFrame(temp)
        temp = temp[[cat,'ConstituentID_x']]
        self.temp = temp
        tsum = temp['ConstituentID_x'].sum()
        temp1 = temp.sort_values(['ConstituentID_x'], ascending=[False], inplace=True)
        temp1 = temp
        temp1['Percent'] = temp1['ConstituentID_x']/tsum * 100
        temp1 = temp1.rename(index = str, columns = {'ConstituentID_x':'Count'})
        temp1 = temp1.head(n=10)
        temp1 = temp1.to_records()
        #print("\tThis thing is a(n): {}  which is a {} class!".format(type(temp1), temp1.__class__.__name__))
        #temp1.describe()
        return temp1
    def des(self):
        dstore = self.temp.describe()
        dstore = dstore.to_records()
        return dstore


def runSearch(someNationality, someDepartment, startDate, endDate):
    print('\tStarting the search')
    df = artworkSet
    df[['Ayear', 'Amonth', 'Aday']] = df['DateAcquired'].str.split('-', expand=True)
    df['Ayear'] = df['Ayear'].replace(np.nan, 0, regex=True)
    df[df['Ayear'] == 'Y'] = 0
    df['Ayear'] = df['Ayear'].astype(str).astype(int)

    country = countrySet

    country = country.rename(index=str, columns={"nationality": "Nationality_y"})
    country = country.rename(index=str, columns={"en_short_name": "Country"})
    df = pd.merge(df,country,how = 'left',on = 'Nationality_y')

    
    Search2 = utilities.inSr(someNationality, someDepartment, startDate, endDate)
    Search2.setup()
    searched = Search2.ret()
    print ("Error time",searched)
    print('\tSetting the filters')
    if searched['inyear'] != 0 and searched['outyear'] != 0:
        filter1 = df[(df['Ayear'] >= searched['inyear']) & (df['Ayear'] <= searched['inyear'])]
    else:
        filter1 = df

    if Search2.blank1() != True and Search2.blank2() != True:
        filter1 = df[(df['Country'] == searched['nation']) & (df['Department'] == searched['dep'])]
    elif Search2.blank1() != True:
        filter1 = df[(df['Country'] == searched['nation'])]
    elif Search2.blank2() != True:
        filter1 = df[(df['Department'] == searched['dep'])]
    else:
        filter1 = df
    print('\tperforming the search')
    results = []
    ddes = []
    ncl = stats(filter1)
    counter = 0
    results.append(ncl.topTen('Artist'))
    ddes.append(ncl.des())
    counter += 1
    #results += str(ncl.des())
    if Search2.blank1() == True:
        results.append(ncl.topTen('Country'))
        ddes.append(ncl.des())
        counter += 1
    if Search2.blank2() == True:
        results.append(ncl.topTen('Department'))
        ddes.append(ncl.des())
        counter += 1
    print ("Walalalalao")
    print (counter)
    print (results)
    with open('searchResults.txt', 'w') as outFile:
        if counter == 1:
            outFile.write('Search Results\n\t{}\n\t{}\n\t{}\n'.format(results[0], results[1], results[2]))
        elif counter == 2:
            outFile.write('Search Results\n\t{}\n\t{}\n'.format(results[0], results[1]))
        else:
            outFile.write('Search Results\n\t{}\n'.format(results[0]))
            
    outFile.close
    with open('searchDes.txt', 'w') as outFile2:
        if counter == 1:
            outFile2.write('Search Results\n\t{}\n\t{}\n\t{}\n'.format(ddes[0], ddes[1], ddes[2]))
        elif counter == 2:
            outFile2.write('Search Results\n\t{}\n\t{}\n'.format(ddes[0], ddes[1]))
        else:
            outFile2.write('Search Results\n\t{}\n'.format(ddes[0]))
            
    outFile2.close
    return results,ddes

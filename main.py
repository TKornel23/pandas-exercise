import pandas as pd
import numpy as np

if __name__ == '__main__':
    # #SERIES
    labels = ['a', 'b', 'c']
    my_data = [10, 20, 30]
    arr = np.array(my_data)
    d = {'a': 10, 'b': 20, 'c': 30}

    print(pd.Series(data = my_data))

    print(pd.Series(data = my_data, index=labels)) #You can specify the indexing
    print(pd.Series(arr))
    print(pd.Series(d)) #key is the index with a dicionary

    print(pd.Series(data=labels))

    ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
    print(ser1)
    ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy', 'Japan'])
    print(ser2)

    print(ser1['USA'])
    ser3 = pd.Series(data=labels)
    print(ser3)

    print(ser1 + ser2)

    # #DATAFRAMES
    from numpy.random import randn

    np.random.seed(101)

    df = pd.DataFrame(data=randn(5,4), index=['A','B','C','D','E'], columns=['W','X','Y','Z'])
    print(df)
    print(df['W'])
    print(type(df['W']))

    print(df[['X','W','Z']])

    df['new'] = (df['W'] + df['Y']) * df['Z']
    print(df)
    df.drop('new', axis = 1, inplace=True)
    print(df)
    print(df.shape)

    print(df.loc['A'])

    print(df.iloc[2])

    print(df.loc[['A','B'], ['W','Y']])

    # #Conditional selections

    booldf = df > 0
    print(booldf)
    print(df[booldf])
    print(df[df > 0])

    print(df['W'] > 0)

    print(df[df['W'] > 0]) #Not returning null

    resultdf = df[df['W'] > 0]
    print(resultdf['X'])

    print(df[df['W'] > 0]['X'])

    # PANDAS EXERCISES

    sal = pd.read_csv("Salaries.csv")
    print(sal.head())
    print(sal.info())
    print(sal['BasePay'].mean())
    print(sal['OvertimePay'].max())
    print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
    print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
    print(sal['TotalPayBenefits'].max())
    print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])
    print(sal.loc[sal['TotalPayBenefits'].idxmax()])
    print(sal.loc[sal['TotalPayBenefits'].idxmin()])
    print(sal.groupby('Year').mean())
    print(sal['JobTitle'].nunique())
    print(sal['JobTitle'].value_counts().head())
    print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))

    def chief_string(title):
        if 'chief' in title.lower().split():
            return True
        else:
            return False

    print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

    sal['title_len'] = sal['JobTitle'].apply(len)
    print(sal[['TotalPayBenefits','title_len']].corr())

    ecom = pd.read_csv("Purchases")
    print(ecom.head())
    print(ecom.info())
    print(ecom['Purchase Price'].max())
    print(ecom['Purchase Price'].min())
    print(ecom['Purchase Price'].mean())
    print(ecom[ecom['Language'] == 'en'].count())
    print(ecom[ecom['Job'] == 'Lawyer'].count())
    print(ecom[ecom['AM or PM'] == 'AM'].count())
    print(ecom['AM or PM'].value_counts())
    print(ecom['Job'].value_counts().head())
    print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])
    print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])
    print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())
    print(ecom[ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25')].count())

    def email_provider(email):
        return email.split('@')[1]

    print(ecom['Email'].apply(lambda x: email_provider(x)).value_counts().head())

"""-->                            CLEANING PANDAS CELLS                      <--"""


"""--> Remove Rows """

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# new_df=df.dropna()                           # Make copy DataFrame copy without Empty cells rows.
# print(new_df.to_string())                    
# print(f"\n\n{df.to_string()}")               # Original DataFrame.

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# df.dropna(inplace=True)                        # Remove Empty cells rows on Original data.                         
# print(df.to_string())


"""--> Replacing Empty Values """

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# df.fillna(130,inplace=True)
# print(df.to_string())


"""--> Replace only for specified columns """

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# df['Calories'].fillna(130,inplace=True)         # Replace null value only in Calories column.
# print(df.to_string())


"""--> Replace using mean, median  and mode. """

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# x=df['Calories'].mean()                        # Recieve mean of whole Calories column values.
# df['Calories'].fillna(x,inplace=True)          # Replace null value from mean only in Calories column.
# print(df)

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# x=df['Calories'].median()
# df['Calories'].fillna(x,inplace=True)
# print(df)

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# x=df['Calories'].mode()[0]
# df['Calories'].fillna(x,inplace=True)
# print(df)


"""-->                            CLEANING Data of Wrong Format                      <--"""



"""--> correction date format """

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# df['Date']=pd.to_datetime(df['Date'])
# print(df.to_string())


"""--> Removing Rows having NaT value """

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# df.dropna(subset=["Date"],inplace=True)
# print(df.to_string())



"""-->                            PANDAS FIXING WRONG DATA                          <--"""


"""--> Replacing value of Data """

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# df.loc[7,'Duration']=45
# print(df.to_string())


"""--> Replacing value of Data """

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# for x in df.index:
#     if df.loc[x,'Duration']>120:
#         df.loc[x,'Duration']=120
# print(df.to_string())


"""--> Removing Rows having wrong data """

# import pandas as pd
# df=pd.read_csv('cdata.csv')
# for x in df.index:
#     if df.loc[x,'Duration']>120:
#         df.drop(x,inplace=True)
# print(df.to_string())



"""-->                            pandas-Removing Duplicates                          <--"""

# import pandas as pd
# df = pd.read_csv('cdata.csv')
# print(df.duplicated())

"""--> Removing Duplicates """

# import pandas as pd 
# df=pd.read_csv('cdata.csv')
# print(df.drop_duplicates())




""".............DATA CLEANING IS OVER NOW............................................................."""

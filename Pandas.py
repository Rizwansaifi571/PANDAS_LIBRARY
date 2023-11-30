"""                   ---> GETTING STARTED WITH Pandas. <---                     """

# import pandas as pd
# print(pd.__version__)



"""                        ---> Pandas Series. <---                              """

# import pandas as pd
# a=[1, 7, 2]
# myvar=pd.Series(a)
# print(myvar)
# print(f"\n{myvar[0]}")


""" --> Create Labels  """

# import pandas as pd
# a=[1, 7, 2]
# myvar=pd.Series(a,index=['x','y','z'])
# print(myvar)
# print(f"\n{myvar['y']}")


""" --> Key/Value objects as Series  """

# import pandas as pd
# calories={'day1':420,'day2':380,'day3':390}
# myvar=pd.Series(calories)
# print(myvar)
# print(f"\n{myvar['day3']}")

# import pandas as pd
# calories={'day1':420,'day2':380,'day3':390}
# myvar=pd.Series(calories,index=['day1','day3'])
# print(myvar)



"""                        ---> Pandas DataFrame. <---                              """


# import pandas as pd
# data={"calories":[420, 380 ,390],"duration":[50, 40, 45]}
# myvar=pd.DataFrame(data)
# print(myvar)
# print(f"\n{myvar.loc[0]}")
# print(f"\n{myvar.loc[[0,1]]}")
# print(f"\n{myvar.loc[[0,1,2]]}")


""" --> Named Index and located Named Index  """

# import pandas as pd
# data={"calories":[420, 380, 390],"duration":[50, 40, 45]}
# df=pd.DataFrame(data,index=['day1','day2','day3'])
# print(df)
# print(f"\n{df.loc['day2']}")



"""                        ---> Pandas Read CSV. <---                              """


# import pandas as pd
# df=pd.read_csv('data.csv')
# print(df.to_string())


""" --> pandas Without to_string  """

# import pandas as pd
# df=pd.read_csv('data.csv')
# print(df)


""" --> Number of Maximum Returned Rows  """

# import pandas as pd
# print(pd.options.display.max_rows)


""" --> Increment of Maximum Returned Rows  """

# import pandas as pd
# pd.options.display.max_rows=170
# df=pd.read_csv('data.csv')
# print(df)
# print("\n\n\n\n")
# print(df.to_string())



"""                        ---> Pandas Read JSON. <---                              """

# import pandas as pd
# df=pd.read_json('data.json')
# print(df.to_string())


""" --> Python Dictionary into DataFrame.  """

# import pandas as pd
# data={
#     "Duration":{
#         "0":60,
#         "1":60,
#         "2":45
#     },
#     "Pulse":{
#         "0":110,
#         "1":117,
#         "2":103
#     }
# }
# df=pd.DataFrame(data)
# print(df)



"""                        ---> Pandas Analysing DataFrame. <---                              """


""" --> Pandas head() method.  """

# import pandas as pd
# df=pd.read_csv("data.csv")
# print(df.head(10))

# import pandas as pd
# df=pd.read_csv("data.csv")
# print(df.head())

""" --> Pandas tail() method.  """

# import pandas as pd
# df=pd.read_csv('data.csv')
# print(df.tail(10))

# import pandas as pd
# df=pd.read_csv('data.csv')
# print(df.tail())

""" --> Pandas info() method.  """

# import pandas as pd
# df=pd.read_csv('data.csv')
# print(df.info())

# import pandas as pd
# df=pd.read_csv('cleandata.csv')
# print(df.info())

# import pandas as pd
# a=pd.read_csv('cdata.csv')
# print(a.to_string())



"""                        ---> Pandas Cleaning Data. <---                              """


import pandas as pd

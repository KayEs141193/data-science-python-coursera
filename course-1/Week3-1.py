########## Merging Dataframes ###########

# Adding new columns

# df['Date'] = [ 'Dec 1', 'Dec 2', 'Dec 3' ] ## Same length as the number of rows
# df['SomeBool'] = True ## Same value supplied to all rows
# df['AnotherColumn'] = pd.Series({'Index1':12,'Index5':13}) ## Values inserted based on index values

# Full Outer Join == Union
# Inner Join == Intersection
# Left Join == all rows on the left with all possible information from right
# Right Join == Analogous to above

# pd.merge(df_left,df_right, how = 'outer', left_index = True, right_index = True)
# pd.merge(df_left,df_right, how = 'outer', left_on = col_left, right_on = col_right)

# left_on and right_on can take list of columns in case joing is to be done using multiple keys

# In case of same columns with different values both are preserved by adding suffixes


########### Pandas Idioms #################

# Idioms: Best ways to solve problems. Pandorable

# 1. Back to back [][] might have wierd behaviour as wey may not know whether reference or copy is being sent
# 2. Chaining is good for methods, as we are returned a reference

############ Group By ################
 # df.groupby(Col) # Can be iterated upon like for group, frame in df.groupby(Col):
 # df.groupby(func).apply(bar,arg2,arg3) # arg1 is the df assosciated with the group

 ########### Scales ###############

 # Ratio Scale, Interval Scale, Ordinal Scale, Nominal Scale
 # Working with categorical data in pandas dtype: category
 # s.astype('category', categories = [c1,c2,c3,c4], ordered = True)
 # pd.cut(df[col1],11, labels = ['Small', 'Medium', 'Large']) # Puts each row into a bin ( out of 11) based on the series provided


 ########### Pivot Tables ################

 # df.pivot_table( values=[c1,c2], index=c2, columns=c3, aggfunc=dict )

 ########### Date Functionality ##############

 # pd.Timestamp
 # pd.Period
 # pd.Timedelta
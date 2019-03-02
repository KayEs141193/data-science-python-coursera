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
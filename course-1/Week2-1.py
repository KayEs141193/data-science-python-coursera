##### Series ######
# Cross between list and dictionary

import pandas as pd
import numpy as np

animals = ['Tiger','Bear','Moose']
s = pd.Series(animals)

# print(type(s))

# for a in s:
# 	print(a)

print(s.dtype)

# Note: NaN is similar to Non e but is a numeric value
# np.nan == np.nan
# np.nan == None
# np.isnan(np.nan)

# creating series from dictionary

sports = { 'Cricket': 'India',
			'Golf': 'Scotland',
			'Baseball': 'USA'}

s = pd.Series(sports)

# Querying a Series

# Both iloc and loc are attributes and not methods, therfore we use [] and not ()
print(s.iloc[2])
print(s.loc['Baseball'])

s[1], s['Golf']

# Use iloc and loc to avoid confusion
# loc can also be used to add elements

s = pd.Series([1,2,3,4,5])

# np.sum(s) is faster than iterating over it, due to vectorization optimizations

cricketLovers = pd.Series({'Cricket':'India',
				 'Cricket':'Australia',
				 'Basketball':'USA'})

cricketLovers = pd.Series( ['India', 'Australia', 'USA'], index = ['Cricket', 'Cricket', 'Basketball'] )

print(type(cricketLovers.loc['Cricket']))
print(type(cricketLovers.loc['Basketball']))
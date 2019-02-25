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

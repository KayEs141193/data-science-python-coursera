########### Datatypes ############

print("DataTypes in Python")

def adder(x,y):
	return x + y

print(type(10))
print(type('abcd'))
print(type(False))
print(type(10.0))
print(type('a'))
print(None)
print(adder)

########### Collection ###########

print("Collections in Python")

# tuple
# Immutable, ordered collection
x = ( 1, 'a', 2, 'b')
print(type(x))

# list
# Mutable, ordered collection
x = [1,'a',2,'b']
print(type(x))

# dictionary
# unordered, labelled collection
x = { "Kushal": 23, "Sam": 22 }
print(x)

########### Strings ###############

# Interesting Functions:

# all list operations are valid
# split, in, [:]

# String formatting language

# CSV manipulation

# import csv

# %precision 2

# with open('mpg.csv') as csvfile:
# 	mpg = list(csv.DictReader(csvfile))
# sum(float(d['cty']) for d in mpg )/len(mpg)

########## Dates and Times ###########

# important libraries
# import datetime as dt
# import time as tm

########## Objects and map() ###########

class Person:
	department = 'ECE' # static datamember

	def set_name(self, new_name):
		self.name = new_name
	def set_location(self, new_location):
		self.location = new_location

x = Person()

# No private or protected members
# no need for constructor but can be created using __init

store1 = [10.0, 11.0, 12.34, 2.34,90]
store2 = [9.0,11.1,12.34,2.01]

# map performs a lazy evalution and returns a map object
cheapest = map(min,store1,store2)

for price in cheapest:
	print(price)
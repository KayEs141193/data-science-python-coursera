# Datatypes

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

# Collection

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
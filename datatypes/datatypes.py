# Number : Additon, Multiplication, Subtraction, Division etc.

x = 10
print(type(x))

x = -10
print(type(x))

x = 10.5  # decimal, float
print(type(x))

x = 10 + 2j # complex number
print(type(x))


# String : concat, replace, trim etc
name = "Raj"
print(type(name))

name = 'Raj'
print(type(name))

name = 'R'  # no concept of character datatype in python
print(type(name))


# Boolean : True/False
taxPaid = True
print(type(taxPaid))

isSunny = False
print(type(isSunny))


# List : collection of items, can be modified
numList = [10, 20, 30, 40, 50]
print((type(numList)))

mixTypeList = [10, 10.5, True, "Raj"]
print(type(mixTypeList))

# Tuple : same as list but cannot be modified
numTuple = (10, 20, 30, 40, 50)
print((type(numTuple)))

mixTypeTuple = (10, 10.5, True, "Raj")
print(type(mixTypeTuple))


# Set : removing duplicates
numSet = {10, 10, 10, 20, 20, 30, 40, 50}
print(numSet)
print(type(numSet))


# Dictionary : key-value
x = {
    "empid" : 1234,  # key : value
    "name" : 'Raj'  # key : value
}

print(type(x))
print(x['empid'])
print(x['name'])
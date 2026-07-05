# create an empty list
cityList = []
print(type(cityList))

# create a list with metro cities names
cityList = ['Mumbai', 'Pune', 'Delhi', 'Kolkatta', '']
print(type(cityList))
print(cityList)

numList = [10, 20, 30, 40, 50]
print(type(numList))
print(numList)

empList = ['Ramesh', 1001, 'Pune', True, 20.5] # Mixed Type
print(type(empList))
print(empList)

# Length of the list
size = len(empList)
print(size)


# Accessing the items
item1 = empList[0] # First Item
print(item1)
print(empList[1])
print(empList[2])
print(empList[3])
print(empList[4]) # Last Item
print(empList[size-1]) # Last Item
# print(empList[5]) #IndexError: list index out of range


# Nested List
empList = ['Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']] # Mixed Type
print(type(empList))
print(empList)
size = len(empList)
print(size)

#Access
firstItem = empList[0] #First
print(firstItem)
print(type(firstItem))
print(empList[1])
print(empList[2])
print(empList[3])
print(empList[4])
lastItem = empList[size-1] # Last Item => ['ML', 'AI', 'DE', 'Python']
print(lastItem)
print(type(lastItem))

# Accessing the lastItem list's item
print(lastItem[0])
print(lastItem[1])
print(lastItem[2])
print(lastItem[3])



# Slicing
# [start:end:step] => defaults => start: 0, end: length, step: 1

#             -6      -5     -4     -3    -2             -1
empList = ['Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']] # Mixed Type
#             0        1      2      3     4              5
print(type(empList))
print(empList)
size = len(empList)
print(size) # length = 6

print(empList[-1]) # ['ML', 'AI', 'DE', 'Python']
print(empList[1:3:1]) # [1001, 'Pune']
print(empList[1:3]) # [1001, 'Pune']
print(type(empList[1:3])) # list
print(empList[1:]) # [1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']]
print(empList[:4]) # ['Ramesh', 1001, 'Pune', True]
print(empList[:]) # ['Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']]
print(empList[::]) # ['Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']]
print(empList[-1][-1]) # 'Python'
print(type(empList[-1][-1])) # <class 'str'>
print(empList[0:4:4]) # 'Ramesh'



# Mutability: ability to modify/change

# insert() => add an element/item to the specific position in the list
# append() => add the item an the end of the list

# name, id, city, isCertified, score, list of expertise
empList = ['Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']] # Mixed Type
print("Before : ", empList)

# add the salary as well
salary = 50000
empList.insert(3, salary)
print("After : ", empList) # ['Ramesh', 1001, 'Pune', 50000, True, 20.5, ['ML', 'AI', 'DE', 'Python']]

# add some identity docs
empList.insert(3, "Aadhaar")
empList.insert(4, "222222222222222")

print(empList) # ['Ramesh', 1001, 'Pune', 'Aadhaar', '222222222222222', 50000, True, 20.5, ['ML', 'AI', 'DE', 'Python']]


# Add identification marks at the end
id_mark = "A birth mark on right hand"
empList.append(id_mark)
print(empList) # ['Ramesh', 1001, 'Pune', 'Aadhaar', '222222222222222', 50000, True, 20.5, ['ML', 'AI', 'DE', 'Python'], 'A birth mark on right hand']

# Add address list (permanent and commincation) to teh list
addressList = ['C-Pune City', 'P-Nagpur City']
empList.append(addressList)
print(empList) # ['Ramesh', 1001, 'Pune', 'Aadhaar', '222222222222222', 50000, True, 20.5, ['ML', 'AI', 'DE', 'Python'], 'A birth mark on right hand', ['C-Pune City', 'P-Nagpur City']]



# iterate over the list

for item in empList:
    print(item)


# Remove an item from list
# remove() : removes the item from list. Error if not present.

# emplList : ['Ramesh', 1001, 'Pune', 'Aadhaar', '222222222222222', 50000, True, 20.5, ['ML', 'AI', 'DE', 'Python'], 'A birth mark on right hand', ['C-Pune City', 'P-Nagpur City']]
# check if an item is present or not in the list and then remove it.

item_to_remove = 'Pune'

if item_to_remove in empList:
    print("Item Found. Removing it now.....")
    empList.remove(item_to_remove)

# empList.remove(item_to_remove)
print(empList)


# pop : remove an item from the end of the list and return the item
# pop(index) : removes an items from teh given index and retrun it

empList = ['Ramesh', 1001, 'Pune', 'Aadhaar', '222222222222222', 50000, True, 20.5, ['ML', 'AI', 'DE', 'Python'], 'A birth mark on right hand', ['C-Pune City', 'P-Nagpur City']]

removedItem = empList.pop()
print(removedItem)
print(empList)

removedItem = empList.pop(0)
print(removedItem)
print(empList)



# List copy

empList = ['Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']]
print(empList)

copiedList = empList # reference copy
print(copiedList)

# Modify original list
empList.remove("Ramesh")
print(empList)
print(copiedList)

#Modify copied list
copiedList.remove(1001)
print(empList)
print(copiedList)


# copy()
empList = ['Ramesh', 1001, 'Pune', True, 20.5, ['ML', 'AI', 'DE', 'Python']]
print(empList)
finalCopiedList = empList.copy() # Separate copy
print(finalCopiedList)

# Modify original list
empList.remove("Ramesh")
print(empList)
print(finalCopiedList)

#Modify copied list
finalCopiedList.remove(1001)
print(empList)
print(copiedList)




# Sorting in the list

cityList = ['Mumbai', 'Pune', 'Delhi', 'Kolkatta', '']
print(cityList)
#cityList.sort()
cityList.sort(reverse=True)
print(cityList)


# List extend
# extend
cityList = ['Mumbai', 'Pune', 'Delhi', 'Kolkatta', '']

extendedCityList = ['Nagpur', 'Chennai']

cityList.extend(extendedCityList)
print(cityList)



cityList.clear()

print(cityList)


del cityList

print(cityList)
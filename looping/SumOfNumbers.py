# WAP that returns the sum of numbers in the list

# numbers = [1, 2, 3, 4, 5, 6, 7]
# O/P: Sum = 28

# len(list) => size of the list

# while loop

numbers = [1, 2, 3, 4, 5, 6, 7]

print(type(numbers))
print("Number of items in the list : ", len(numbers))

sum = 0
noOfItems = len(numbers)
pos = 0 # initialization

while pos <= noOfItems-1 :
    sum = sum + numbers[pos]
    pos = pos + 1

print("Sum (while) = ", sum)



# for loop

sum = 0

for num in numbers:
    sum = sum + num

print("Sum (for) = ", sum)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# range(start, stop, [step]) => Generator Function => generates => sequence of numbers
# range(1, 10) => iterable
print(range(1, 10))
print(type(range(1,10)))

for num in range(0, 10):
    print(num)




numbers = [1, 2, 3, 4, 5, 6, 7]  # startPos = 0, endPos = 6
sum = 0
for pos in range(0, len(numbers)):  # range(0, 7) => 0, 1, 2, 3, 4 ,5, 6
    sum = sum + numbers[pos]

print("sum (for-index) : ", sum)


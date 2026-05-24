num = int(input("Enter a number : "))  # 2
terms = int(input("Enter no of terms : ")) # 5


# 2 * 1 = 2
# 2 * 2 = 4

# num * sequence = multiplication_result


# while 
i = 1

while i<=terms:
    print(num, '*', i, ' = ', num * i) # 2 * 1 = 2
    i = i + 1

# for
for i in range(1, terms+1):
    print(num, '*', i, ' = ', num * i) # 2 * 1 = 2


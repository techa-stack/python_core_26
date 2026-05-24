# (5! = 5 * 4 * 3 * 2 * 1 = 120)

# Approach 1
num = 5
factorial = 1 # to store the final outcome

while num >= 1: # 1 >=1
    factorial = factorial * num # 120 * 1 = 120
    num = num - 1 # 0

print("Factorial (num decremnt): ", factorial)


# Approach 2
num = 5
factorial = 1 # to store the final outcome

i = 1

while i<= num: # 1 >=1
    factorial = factorial * i # 120 * 1 = 120
    i = i + 1

print("Factorial (ascending) : ", factorial)



# for
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial (for) =", factorial)
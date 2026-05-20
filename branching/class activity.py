# 1. Speed Tracker
# You are driving a car
# Speed sensors track the speed

# <30 km/hr => Very Slow
# >=30 and <50 => Average speed
# >=50 and <80 => Fast but under the limits
# >=80 => Fined


# User input : speed
# print the message accordingly


#speed = float(input("Enter the speed (km/hr): "))
speed =30
if speed < 30:
    print("Very Slow")
elif speed >= 30 and speed < 50:
    print("Average speed")
elif speed >= 50 and speed < 80:
    print("Fast but under the limits")
else:
    print("Fined")



# 2. Design a Login System

#Ask for:
#    username
#    password
# Check against predefined values and print:

# O/P :
#   "Login successful"
#   "Invalid credentials"



# 3. Voting Eligibility with Conditions

# Input:
#   age
#   citizenship (yes/no)

# Output:
#   Print if the person is eligible to vote.




# 4. Simple Calculator (No loops)

# Input:
#   two numbers
#   one operator (+, -, *, /)

# Output : Value after applying the operator
# Use branching to perform the operation.


num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
op = input("Enter the operator (+, -, *, /) :")

#print(num1, op, num2)

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

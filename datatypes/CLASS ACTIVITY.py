#You are driving a car
#Speed sensors

#<30 km/hr => Very Slow
#>=30 and <50 => Average speed
#>=50 and <80 => Fast but under the limits
#>=80 => Fined

#User input : speed
#print the message accordingly

x =float(input ("enter speed"))
if x<30:
    print("very slow")
elif x>=30 and x<50:
    print("average speed")
elif x>=50 and x<80:
    print("fast but under the limits")
else:
    print("fined")

#Design a Login System

# Ask for:
#username
#password
#Check against predefined
#values and print:

#O / P:
#"Login successful"
#"Invalid credentials



username =input ("enter username")
password = input ("enter password")

if username == "sparsh@123" and password == "1234":
    print("login successful")
else :
    print ("login faield")

#Input:
#age
#citizenship(yes / no)

#Output:
#Print if the
#person is eligible
#to
#vote.
age = int(input ("enter age"))
citizenship = input ("enter citizenship")

if age >= 18 and citizenship == "yes":
    print("person is eligible to vote")
else:
    print("person is not eligible to vote")

    # Simple Calculator (No loops)

#Input:#Simple Calculator (No loops)

#Input:
#two numbers
#one operator (+, -, *, /)

#Output : Value after applying the operator
#Use branching to perform the operation.

x = int(input ("enter 1st number:"))

y = int(input ("enter 2nd number:"))

operator = (input("enter thr operator(+, -, *, /):"))
if operator == "+":
    print(x+y)
elif operator == "-":
    print (x-y)
elif operator == "*":
    print (x*y)
elif operator == "/":
    print (x/y)
else :
    print ("invalid operator")



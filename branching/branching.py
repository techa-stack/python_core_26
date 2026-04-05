x = -10

# Check if the value is +ve

# x > 0 => True (Boolean)

# x = 0 => 0 (not a boolean, cannot be used in decision making statements)
# x == 0 => True/False

# if : will be executed only when the condition is True
# else : will be executed when the IF condition is not true

#  :          => marks the beginning of the body
# indentation =>

if x > 0:
    print("Number is +ve")
else:
    print("Number is not positive")


# > +ve, < -ve, == 0

# approach 1 : only if

x = 10

if x > 0:
    print("Number is +ve")
if x < 0:
    print("Number is -ve")
if x == 0:
    print("Zero value")


# Approach 2 : if ....elif

if x > 0:
    print("Number is +ve")
elif x < 0:
    print("Number is -ve")
elif x == 0:
    print("Zero value")


# Approach 3 : if ....elif...else

if x > 0:
    print("Number is +ve")
elif x < 0:
    print("Number is -ve")
else:
    print("Zero value")


# Approach 4 : if ...else (nested)

if x > 0:
    print("Number is +ve")
else:
    if x < 0:
        print("Number is -ve")
    else:
        print("Zero value")



# check if number is +ve and multiple of 2 (nesting use case)
x = -101

# Approach 1
if x > 0:
    print("Number is +ve")
    if x%2 == 0:
        print("Multiple of 2")
    else:
        print("Not a multiple")
else:
    if x < 0:
        print("Number is -ve")
    else:
        print("Zero value")

print("End of block")


# Approach 2 :
if x > 0 and x % 2 == 0 :
    print("Number is +ve and multiple of 2 ")
else:
    print("Not a multiple")


# get a number from user and display

x = input("Please enter a number : ")  # when run, pause the program, wait the user input
print("user input is : ", x)
# check and convert/error out
print(type(x))


x = int(input("Please enter a number : "))  # explicit typecasting
print("user input is : ", x)
print(type(x))

x = float(input("Enter Currency conversion rate (USD to INR) : "))
print("user input is : ", x)
print(type(x))
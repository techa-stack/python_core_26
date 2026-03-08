import keyword

kwrds = keyword.kwlist
print("No of keywords in python : ", len(kwrds))
print(kwrds)

response = "hello" in kwrds # Checking if "hello" is present in the keyword list  Response : True/False
print(response)

response = "while" in kwrds # True/False
print(response)

response = "true" in kwrds # True/False
print(response)

response = "True" in kwrds # True/False
print(response)
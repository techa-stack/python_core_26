# id()

x = 10
print(x)
print(type(x))
print("Location of x is ", id(x))
print(type(id(x)))


# addressof

from ctypes import c_int, addressof
print("Location of x based on addressof ", addressof(c_int(x)))
print(type(addressof(c_int(x))))

x = 10
y = 10
z = 20

print(x is y) # memory location check
print(x is z) # memory location check

print(x is not z)

x = [10, 20]
y = [10, 20]

print(x is y) # memory location check
print(x == y) # value check

z = x

print(x is z)


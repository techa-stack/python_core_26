# ISO
# ASCII
# UNICODE

name = "Raj"
print(type(name))
print(name)

name = 'Raj'
print(type(name))
print(name)

name = "Hello Everyone !"
print(type(name))
print(name)

name = ("Hello "
        "Everyone !")
print(type(name))
print(name)

name = "Hello " \
        "Everyone !" \
        "How are you ?"
print(type(name))
print(name)

name = """Hello  
        Everyone !
        How are you ?"""
print(type(name))
print(name)

name = '''Hello  
        Everyone !
        How are you ?'''
print(type(name))
print(name)


program = '''
if x > 0:
    print("Number is +ve")
else:
    if x < 0:
        print("Number is -ve")
    else:
        print("Zero value") '''

print(program)



name = "Hello !"
print(type(name))
print(name)

# Accessing the charcters, 0-indexed based
print(name[0]) # First character
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6]) # Last character

# Length of the string
length = len(name)
print("Length of the string is ", length)

lastIndex = length - 1
print("Last Index Position ", lastIndex)

# Access last character
print(name[lastIndex]) # +ve indexing

# -ve indexing
print(name[-1]) # -ve indexing, last character
lastNegativeIndex = -1 * length
print("First Character ", name[lastNegativeIndex])



# String Slicing

greet = "Hello Ramesh !"
N = len(greet)
print("Length of the string ", N)

print("First Character ", greet[0])
print("Last Character ", greet[N-1])
print("Last Character ", greet[-1])

# Slicing Approach 1 : greet[start:stop:step]
# start => starting index position, default : 0
# stop => end index position, excluded from o/p, default : entire length
# step => increment, default 1

print(greet[0:3]) # start: 0, stop : 3, step: 1 (default as no value is provided)
print(greet[0:3:1]) # start: 0, stop: 3, step: 1
print(greet[0:3:2]) # start: 0, stop: 3, step: 2

print(greet[3:10]) # start:3, stop: 10, step: 1(default)
print(greet[:10]) # start:0(default), stop: 10, step: 1 (default)
print(greet[:10:]) # start:0(default), stop: 10, step: 1 (default)
print(greet[::]) # start:0, stop: length of string, step: 1
print(greet[::2]) # start:0, stop: length of string, step: 2

print(greet[-14:-8]) # start: -14, stop: -8, step: 1
print(greet[-4:]) # start: -4, stop: length, step: 1
print(greet[:-4]) # start: 0, stop: -4, step: 1

print(greet[:]) #

print(greet[-8:-14])


print(greet[-15]) #IndexError: string index out of range
print(greet[15])  #IndexError: string index out of range


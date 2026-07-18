# create an empty dictionary

adict = {}
print(type(adict))

adict = dict()
print(type(adict))

equipment = {
    "brand" : "Tata",  # key : value
    "year" : 2025,      # key : value
    "model": "X-553535" # key : value
}

print(equipment)
print(type(equipment))

print(len(equipment)) # length of dictionary

for key in equipment:
    print(key, equipment[key])


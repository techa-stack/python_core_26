# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20



rows = 4
cols = 5
i = 1

num_to_print = 1

while i <= rows:
    j = 1
    while j <= cols:
        print (num_to_print, end=" ")
        j = j + 1
        num_to_print = num_to_print + 1
    print()
    i = i + 1



# 1 3 5 7 9
# 11 13 15 17 19
# 21 23 25 27 29
# 31 33 35 37 39

rows = 4
cols = 5
i = 1
j = 1

while i <= rows:
    temp = 1
    while temp <= cols:
        print (j, end=" ")
        j = j + 2
        temp = temp + 1
    print()
    i = i + 1
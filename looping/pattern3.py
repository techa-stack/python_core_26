# 1 1 1 1 1
# 2 2 2 2 2
# 1 1 1 1 1
# 2 2 2 2 2


rows = 4
cols = 5
i = 1

while i <= rows:
    j = 1
    while j <= cols:
        if i%2 == 0:
            print("2 ", end = " ")
        else:
            print("1 ", end = " ")
        j = j + 1
    print()
    i = i + 1
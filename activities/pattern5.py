rows = 4
cols = 5
i = 1

while i <= rows:
    j = 1
    while j <= cols and i%2!=0:
        print (j, end=" ")
        j = j + 1

    temp = cols
    while temp >=1 and i%2==0:
        print (temp, end=" ")
        temp = temp - 1

    print()
    i = i + 1
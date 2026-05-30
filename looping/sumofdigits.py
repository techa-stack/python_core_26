# 1234 = 1 + 2 + 3 + 4

num =  123456789
sum = 0

while num > 0:
    r = num % 10
    sum = sum + r  # 0 + 6 = 6
    num = num // 10

print ("sum of digits : ", sum)

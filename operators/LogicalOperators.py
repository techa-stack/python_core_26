# play = (weather = not raining) AND (time= evening)

#fine but time is 8 pm # no play , False
#raining but time 5pm # no play, False
#not raining and 5 pm # go, True


#play = weather = not raining OR time= evening
#fine but time is 8 pm # play True
#raining but time 5pm # play
#not raining and 5 pm # play
#raining and time is 8 pm # no play False


# and, or, not
# and : Returns True, if all the conditions/statements are true
# or :  Return True, if any of the condition/statement is True
# not : reverses the boolean outcome


x = 4

print(x< 10) # True
print(x == 5) # False
print(x == 4) # True


print((x < 10) and (x==5)) # True and False, OP : False
print((x < 10) and (x==4)) # True and True, Op: True
print((x==5) and (x>1)) # False and True , OP: False


print((x < 10) or (x==5)) # True or False, OP : True
print((x > 10) and (x==5)) # False or False, Op: False
print( (x>30) or (x==4) ) # False or True, OP : True

print((x>1) or (x>2)) # True or True , OP : True

# NOT
print(not((x>1) or (x>2))) # True or True , OP : True







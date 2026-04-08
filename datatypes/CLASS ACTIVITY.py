#You are driving a car
#Speed sensors

#<30 km/hr => Very Slow
#>=30 and <50 => Average speed
#>=50 and <80 => Fast but under the limits
#>=80 => Fined

#User input : speed
#print the message accordingly

x =float(input ("enter speed"))
if x<30:
    print("very slow")
elif x>=30 and x<50:
    print("average speed")
elif x>=50 and x<80:
    print("fast but under the limits")
else:
    print("fined")

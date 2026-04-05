# You are driving a car
# Speed sensors track the speed

# <30 km/hr => Very Slow
# >=30 and <50 => Average speed
# >=50 and <80 => Fast but under the limits
# >=80 => Fined


# User input : speed
# print the message accordingly


speed = float(input("Enter the speed (km/hr): "))

if speed < 30:
    print("Very Slow")
elif speed >= 30 and speed < 50:
    print("Average speed")
elif speed >= 50 and speed < 80:
    print("Fast but under the limits")
else:
    print("Fined")
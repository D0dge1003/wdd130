#Heart Rate Assignment
#Input patient age
age = int(input("Please Enter Age:  "))
#determine the slowest and fastest rates necessary to 
# strengthen his heart.
# (220-Age)=(maximum bpm)
x = 220
max_heart_rate = x - age
# to exercise and to strengthen heart, between 65%(.65) 
# and 85%(.85) of (Max BPM)
minBPM= max_heart_rate * 0.65
maxBPM= max_heart_rate * 0.85
print(f"When you exercise to strengthen your heart, you should keep your heart between {minBPM:.0f} and {maxBPM:.0f} beats per minute. ")
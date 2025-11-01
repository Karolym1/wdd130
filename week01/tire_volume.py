import math
from datetime import datetime

width= float(input("Enter the tire width in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter= float(input( "Enter the diameter of the wheel in inches (ex 15): " ))

volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
print(f"The approximate volume is {volume:.2f} litters")
#Current date (without time)
today = datetime.now()



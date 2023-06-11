import math

a = int(input())
b = int(input())

angle_radians = math.atan2(b, a)
angle_degrees = math.degrees(angle_radians)

print(round(angle_degrees))

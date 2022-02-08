import math
name = "Pranij Joshi"
add = "Bhainsepati"
print(f"Hello, my name is {name} and I live in {add}.")
radius = 7
print(f"The radius of the circle with radius {radius} is {math.pi * radius * radius:.2f}")
student = {"John": 7, "Eric": 98, "Terry" : 100}
for n in student:
    print(f"{n:8} -------> {student[n]:4d}")

print("Your name is {}, and your address is {}".format(add, name))
print("Your name is {1}, and your address is {0}".format(add, name))
print("1. 3 types are int, float, complex")
x = 1    # int
y = 2.8  # float
z = 1j   # complex
p = -87.7e100 # float 

print(type(x))
print(type(y))
print(type(z))
print(type(p))

print("2. Complex numbers are written with a 'j' as the imaginary part")
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

print("3. To convert from one type to another, you can use the int(), float(), and complex() functions")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print("You cannot convert complex numbers into another number type.")

print("4. Random number")
import random
print(random.randrange(100,1000))

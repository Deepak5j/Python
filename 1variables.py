#1 creating variables.............
x = 5
y = 'Deepak'
print(x)
print(y)

#2 casting variables.............
x = str(3)
y = int(3)
z = float(3)
print(type(x))
print(type(y))
print(type(z))

#3 Get the type.............
x = 5
y = 'Deepak'
print(type(x))
print(type(y))

#4 Single or double quotes.............
x = "Deepak"
y = 'Deepak'
print(x, type(x), end = ' \n')
print(y, type(y), end = ' ')

#5 Case-sensitive.............
a = 4
A = 'Deepak'
print(a == A) # False

#6 Variable names.............
# Legal variable names:
myvar = "Deepak Gautam"
my_var = "Deepak Gautam"
_my_var = "Deepak Gautam"
myVar = "Deepak Gautam"
MYVAR = "Deepak Gautam"
myvar2 = "Deepak Gautam"

#7 Variable name formats
# camelCase
myVariableName = "Deepak Gautam"
# PascalCase
MyVariableName = "Deepak Gautam"
# sanke_case
my_variable_name = "Deepak Gautam"
# camelCase case mostly used in JAVA, C, C++, Python
# snake case mostly used in Python, Ruby, PHP

#8 assigin multiple variables at once.............
x, y, z = 'Deepak', 'Gautam', 'Python'
print(x, y, z) 

#9 unpacking a collection variable............. 
names = "Deepak", "Gautam", "Python"
x, y, z = names
print(x, y, z)

#10 Python Output .............
# print() function used for console output
x = "Deepak Gautam"
print("Hello, World!", x)
print("Hello"," World!", x) # comma separated multiple values
print("Hello" + " World!" + x) # concatenate multiple values
# + operator is for addition and for concatination
# but values must be compariable for +
# print("Hello" + 5) # TypeError: can only concatenate str (not "int") to str

#11 Global Variables.............
x = "Deepak Gautam"
def output():
    print("Hello, World!", x) # accessing global variable
output()

# when a local variable have same name as global    
x = "Deepak Gautam"
def output():
    x = "Python"
    print("Hello, World!", x) # accessing global variable
print(x) 
output()

# Global Keyword.............
x = "Deepak Gautam"
def output():
    global x 
    x = "Python"
    print("Hello, World!", x) # accessing global variable
print(x) 
output()
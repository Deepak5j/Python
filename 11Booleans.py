print('1.Boolean Values')
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print('b is greater than a')
else:
    print('b is not freater than a')
    
print('value and variable evaluation')
print(bool('Hello'))
print(bool(15))

print('\n2.Most Values are True')
print(bool('abc'))
print(bool(123))
print(bool(['apple', 'banana', 'cherry']))

print('\n3.Some Values are False')
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print('\n4.Functions can Return a Boolean')
def myFunction() :
    def __len__(self):
        return 0
obj = myFunction()
print(bool(obj))

print('\n5.Using the bool() Function')
def myFunction() :
    return True
print(myFunction())


def myFunction() :
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")
    
print('\n6. isinstance() Function')
x = 200
print(isinstance(x, int))
print(isinstance(x, str))


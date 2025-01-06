# 'Deepak' is same as "Deepak"
# OR 'D' is same as "D"
print('Deepak')
print("Deepak")

print("one single quote ' inside double quote")
print("two single quote 'XXX' insdie a double quote")
print('two double quote inside "xxx" a single quote')

a = 'Deepak'
print(a)

a = '''This
is
a 
multiline
string.
It is 
mostly used for 
documentation 
or comments.
'''
print(a)

print('\nAs array')
a = 'Hello, World!'
print(a[7])

print('\n Looping to string')
for i in a:
    print(i)
    
print('\n String length')
print(len(a))
    
print('\nchecking in string')
print('world' in a)
print('World' in a)

print('\nusing if ')
if 'World' in a:
    print('World present in ', a)
    
print('\n not keyword')
print('world' not in a)
print('World' not in a) 

print('using if with not')
if 'world' not in a:
    print('No, world is not in present in ', a)




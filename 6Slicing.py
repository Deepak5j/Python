# defining a string for operation
a = 'Hello, World!'

print('1.Slicing from a index to index')
print(a[7:12])

print('\n2.Slicing from start to index')
print(a[:5])

print('\nSlicing from index to end')
print(a[7:])

print('\nNegative indexing')
doc = '''
h     e    l    l   o   ,   _   W   o   r   l   d  !
0     1    2    3   4   5   6   7   8   9   10  11 12
-13 -12  -11  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 

In Python slicing, the general syntax is a[start:stop]

For last chracter ==> a[12:13] or a[-1:]
'''
print(doc) 
print(a[-13:-8])
print(a[-6:-1])
print(a[-1:]) # starting from last index to blank, means end.

 



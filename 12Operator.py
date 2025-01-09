print(10 + 5)

print('1.Arithmetic Operators')
print('Addition',10 + 5)
print('Subtraction',10 - 5)
print('Multiplication',10 * 5)
print('Division',10 / 5)
print('Floor Division',10 // 3)
print('Modulus',10 % 3)
print('Exponentiation',10 ** 3)

print('\n2.Assignment Operators')
print('=')
print('+=')
print('-=')
print('*=')
print('/=')
print('//=')
print('%=')
print('**=')
print('&=') 
print('!=')
print('^=')
print('>>=')
print('<<=')
print(':=')
print(x:=3)

print('\n3.Comparison Operators')
print('==')
print('!=')
print('>') 
print('<')
print('>=')
print('<=')

print('\n4.Logical Operators')
print('and 1<10 and 3<10', 1<10 and 3<10)
print('or 1>5 or 3<10', 1>5 or 3<10)
print('not 1<5', not(1<5))

print('\n5.Identity Operators')
print('is not')
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x is not y)
print(x != y)
print('is')
print(x is z)
print(x is y)
print(x == y)

print('\n6.Membership Operators')
print("banana" in x)
print("pineapple" not in x)

print('\n7.Bitwise Operators')
print('& AND')
print(6 & 3)
'''
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
'''

print('| OR')
print(6 | 3)
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print('^ XOR')
print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""











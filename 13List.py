print('1. List')
ls = ['apple', 'banana', 'cherry']
print(ls)

ls = ["apple", "banana", "cherry", "apple", "cherry"]
print('\n2.list with dublicate items: \n', ls)

print('\n3.Length of above list: ', len(ls))

print('\n4. Access Items, using index, at index 1')
print(ls[1])

print('\n5. Negative Indexing, at index -1')
print(ls[-1])

print('\n6.Data types')
ls1 = ["apple", "banana", "cherry"]
ls2 = [1, 5, 7, 9, 3]
ls3 = [True, False, False]
print('String List: ', ls1)
print('Integer List: ', ls2)
print('Boolean List: ', ls3)

print('\n7. type()')
print(type(ls1))
print(type(ls2))
print(type(ls3))

print('\n8. The list() Constructor')
ls4 = list(("apple", "banana", "cherry"))
print(ls4)
ls5 = list((1,2))
print(ls5)

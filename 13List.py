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

print('\n9. Insert Items')
print('Before Insert: ', ls4)
ls4.insert(1, 'orange')
print('After Insert: ', ls4)

print('\n10. Append Items')
print('Before Append: ', ls4)
ls4.append('orange2')

print('\n11. Extend List')
print('Before Extend: ', ls4)
print('Before Extend: ', ls5)
ls4.extend(ls5)
print('After Extend: ', ls4)

print('\n12. Adding any iterable')
ls6 = [11, 22, 33, 44, 55]
ls4.extend(ls6)
print('After Extend: ', ls4)

print('\n13. Remove Item')
ls4.remove(11)
ls4.remove(44)
ls4.remove(55)
print('After Remove: ', ls4)

print('\n14. removing by index')
ls4.pop(1)
ls4.pop(6)
print('After Remove: ', ls4)

print('\n15. pop() removing last by default')
ls4.pop()
print('After Remove: ', ls4)

print('\n16. del keyword')
del ls4[0]
print('After Remove: ', ls4)
del ls4[3:4]
print('After Remove: ', ls4)
del ls4
# print('After Remove: ', ls4) # NameError: name 'ls4' is not defined

print('\n17. clear()')
print('After Clear: ', ls5)
ls5.clear()
print('After Clear: ', ls5)





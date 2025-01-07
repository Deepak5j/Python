print('1.concatination required both value to be string')
print('use str() constructor function')
age = 33
# txt = 'My name is Deepak Gautam, I am ' + age
txt = 'My name is Deepak Gautam, I am ' + str(age) + ' years old.'
print(txt)

print('\n2.F-String')
txt = f'My name is Deepak Gautam, I am {age} years old.'
print(txt)

print('\n3.Placeholders')
price = 59
txt = f'The price is {price} dollers'
print(txt)
print(f'f-string Placeholder can have executable code too {2**3}')

print('\n4.Modifiers')
price = 60.5123 
txt = f'The price is {price:.2f} dollers'
print(txt) 
txt = f'The price is {price:.4f} dollers'
print(txt) 





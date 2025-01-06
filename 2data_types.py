print("1. Built in data types.............")
print("text type values:- str")
print("numeric type values:- int, float, complex")
print("sequence type values:- list, tuple, range")
print("mapping type values:- dict")
print("set type values:- set, frozenset")
print("boolean type values:- bool")
print("binary type values:- bytes, bytearray, memoryview")
print("None type values:- None")    

print("\n2. Getting the data type.............")
x = "Deepak Gautam"
print("'Deepak Gautam' is ",type(x))
x = 5
print("5 is ",type(x))
x = 5.5
print("5.5 is ",type(x))

print("\n3. Setting the data type and setting specific data type.............")    
a1 = str("By str() function Deepak Gautam") #stri
a2 = "By string valur Deepak Gautam" #str
b1 = 1 #int
b2 = int(1) #int
c1 = 2.5 #float
c2 = float(2.5) #float
d1 = 3j #complex
d2 = complex(3j) #complex
e1 = list(("Deepak", "Gautam", "Python")) #list
e2 = ["Deepak", "Gautam", "Python"] #list
f1 = tuple(("Deepak", "Gautam", "Python")) #tuple
f2 = ("Deepak", "Gautam", "Python") #tuple
g1 = range(6) #range
g2 = range(2, 6) #range
h1 = dict(name="Deepak", age=22) #dict
h2 = {"name": "Deepak", "age": 22} #dict
i1 = set(("Deepak", "Gautam", "Python")) #set
i2 = {"Deepak", "Gautam", "Python"} #set
j = frozenset(("Deepak", "Gautam", "Python")) #frozenset
k1 = bool(5) #bool
k2 = False #bool
l1 = bytes(6) #bytes
l2 = b'Hello' #bytes
m = bytearray(7) #bytearray
n = memoryview(bytes(7)) #memoryview
t = None #None
for i in [a1,a2,b1,b2,c1,c2,d1,d2,e1,e2,f1,f2,g1,g2,h1,h2,i1,i2,j,k1,k2,l1,l2,m,n,t]:
    print(i, type(i))
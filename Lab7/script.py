#Tuples

#1 #2 Create a tuple, mixed data types

tupl = (1,2,3,"Hello")
print(tupl)

#3 print one item in tuple
print(tupl[1])

#4 unpack a tuple in several variables
x=10
y=20
print(f'x={x},y={y}')

x,y = y,x
print(f'x={x},y={y}')

#5 add an item to tuple
tupl = (1,2,3)
a1 = "Hi"
print(tupl)
tupl = tupl + (a1,)
print(tupl)

#6 convert tuple to string
tuple = ('i','s','h','a','n')
str = ''.join(tuple)
print(str)

#7 4th and 4th last element from a tuple
tup = 1,2,3,4,5,6,7,8,9,0,'i','s','h','a','n'
print(tup[4],tup[-4])

#8 duplicates in tuple
tup=(1,3,4,32,1,1,1,31,32,12,21,2,3)  
for i in tup:
    if tup.count(i) > 1:
        print(i)

#9 find if element exists in a tuple
Atuple = [('Mon',10),('Tue',8),('Wed',8),('Thu',5)]
print("Given tuple: ",Atuple)
if any('Tue' in i for i in Atuple):
   print("present")
else :
   print("Not present")


# Convert list to tuple
def convert(list):
    return tuple(list)
list = [1, 2, 3, 4]
print(convert(list))


# delete an item from tuple
import numpy as np

tuplex = (1,2,3,4,5)
print(tuplex)
tuplex = np.array(tuplex)
tuplex = np.delete(tuplex, [1])
print(tuplex)
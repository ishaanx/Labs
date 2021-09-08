#1. Write a Python program to sum all the items in a list. 

list = [5,5]
print(sum(list))

#2. Write a Python program to multiplies all the items in a list.

import math
list = [5,5]
print(math.prod(list))

#3. Write a Python program to get the largest number from a list. 

list = [1,2,3,4,5]
print(max(list))

#3. Write a Python program to get the smallest number from a list. 

list = [1,2,3,4,5]
print(min(list))

#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

def func1():
    list = ['abc', 'xyz', 'aba', '1221']
    counter = 0
    for x in list:
        if len(x) > 1 and x[0] == x[-1]:
            counter +=1
    print(counter)   
func1()


#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=lambda x:x[1])

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#7. Remove duplicate from list

list = [1, 3, 5, 6, 3, 5, 6, 1]
newList = []
[newList.append(x) for x in list if x not in newList]
print(newList)

#8. check if list is empty

l2 = []
if not l2:
    print("List is empty")
else:
    print("List is not empty")

#9. Write a Python program to clone or copy a list. 
oldList = [1,2,3,4,5]
newlist = oldList.copy()
print(newlist)

#10. Write a Python program to find the list of words that are longer than n from a given list of words. 

def long_words(n, str):  
    word_len = []  
    txt = str.split(" ")  
    for x in txt:  
        if len(x) > n:  
            word_len.append(x)  
    return word_len   
print(long_words(3, "The quick brown fox jumps over the lazy dog")) 

#11. compare two lists and return true if even 1 object matches

def compare_lists(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(compare_lists([1,2,3,4],[5,6,7,0]))

#12 Write a Python function that takes two lists and returns True if they have at least one common member. 
list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print ('Original list is :',list1)
del list1[5]
del list1[4]
del list1[0]
print('Modified list is: ',list1)

#13 3d array
symbol = [[ ['*' for col in range(3)] for col in range(4)] for row in range(6)]
print(symbol)

#14 remove even numbers from list
list = [1,2,3,4,5]
print("Original List")
print (list)
for x in list:
    if(x%2==0):
        list.remove(x)
print("New list is: ",list)

#15 Shuffle a list
import random
list = [1,2,3,4,5]
print("Original list is: ",list)
random.shuffle(list)
print("Shuffled list is: ",list)

#16 

def printValues():
	l = []
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()

#17 
def printValues2():
	l = []
	for i in range(1,21):
		l.append(i**2)
	print(l[5:])
	print(l[:-5])

printValues2()

# 18 all permutations
from itertools import permutations 
  
  
a = "Ishan"
  
# no length entered so default length
# taken as 4(the length of string GeEK)
p = permutations(a) 
  
# Print the obtained permutations 
for j in list(p): 
    print(j)

#19 difference between two lists
list_1 = [5, 10, 15, 20, 25, 30]
list_2 = [10, 20, 30, 40, 50, 60]

difference_1 = set(list_1).difference(set(list_2))
difference_2 = set(list_2).difference(set(list_1))

list_difference = list(difference_1.union(difference_2))
print(list_difference)


#20 Access index of a list
mylist = [21, 5, 8, 52, 21, 87]
item = 8

#search for the item
index = mylist.index(item)

print('The index of', item, 'in the list is:', index)
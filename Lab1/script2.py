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
# Lab 8/9/10

# Write a Python script to merge two Python dictionaries. 
# using | operator

def merge(dict1, dict2):
    result = dict1 | dict2
    return result

dict1 = {'one':1,'two':2,'three':3,'four':4}
dict2 = {'five':5,'six':6,'seven':7,'eight':8}
dict3 = merge(dict1,dict2)
print("Merged dict is {0}".format(dict3))

# Write a Python program to remove duplicates from Dictionary.
dict1 = {'one':1,'two':2,'three':3,'four':4,'four':4}
temp=[]
result = dict()
for key,value in dict1.items():
    if value not in temp:
        temp.append(value)
        print(temp)
        result[key]=value

print(result)

# Write a Python program to find the highest 3 values in a dictionary. 

from collections import Counter
dict1 = {'one':1,'two':2,'three':3,'four':4}

k = Counter(dict1)
high = k.most_common(3)

print('Original dict:')
print(dict1,"\n")

print('3 highest values:')
print(high)

#
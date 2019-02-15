'''
    Python dictionary is a container of the unordered set of objects like lists.

    The objects are surrounded by curly braces { }.

    The items in a dictionary are a comma-separated list of key:value pairs
    where keys and values are Python data type.

    Each object or value accessed by key and keys are unique in the dictionary.

    As keys are used for indexing, they must be the immutable type (string, number, or tuple).
    You can create an empty dictionary using empty curly braces.
'''

# create Empty Dictionary
new_dict1 = dict()
new_dict2 = {}
print(new_dict1)
print(new_dict2)

color ={'col1': 'red','col2': 'green','col3': 'blue'}
dict = {1: 20.5, 2: 3.03, 3: 23.22, 4: 33.12}
print(color['col1'])
print(color)
# ways to access dictonary data
print(dict[4])
print(dict.get(4))


# Add key/value to a dictionary
dic = {'pdy1':'DICTIONARY'}
print(dic)
# dic['pdy1'] = 'char'
dic['pdy2'] = 'STRING'
print(dic)

# Using update() method to add key-values pairs in to dictionary
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


# Iterate over Python dictionaries using for loops
d = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in d.items():
  print(color_key, "corrospond to", d[color_key])

# Remove a key from a Python dictionary
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(myDict)
if 'a' in myDict:
  del myDict['a']
print(myDict)

# sort a python Dictionary by key
color_dict = {'2': '#FF0000',
              '4': '#008000',
              '1': '#000000',
              '3': '#FFFFFF'}
print(color_dict)
for key in sorted(color_dict):
  print('%s:%s' % (key, color_dict[key]))

# Find the maximum and minimum value of a Python dictionary
my_dict = {'x': 500, 'y': 5874, 'z': 560}
print(max(my_dict.keys(), key=(lambda k: my_dict[k])))
print(min(my_dict.keys(), key=(lambda k: my_dict[k])))

# Concatenate two Python dictionaries into a new one
dic1={1: 10, 2: 20}
dic2={3: 30, 4: 40}
dic3={5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3) : dic4.update(d)
print(dic4)


# Test whether a Python dictionary contains a specific key
fruits = {}
fruits["apple"] = 1
fruits["mango"] = 2
fruits["banana"] = 4
print(fruits)
# Use in.
if "mango" in fruits:
    print("Has mango")
else:
    print("No mango")

# Use in on nonexistent key.
if "orange" in fruits:
    print("Has orange")
else:
    print("No orange")


# Find the length of a Python dictionary
fruits = {"mango": 2, "orange": 6}
# Use len() function to get the length of the dictionary
print("Length:", len(fruits))



#List of Dictionary
list1 =[{"id": "1", "name": "Manish"}, {"id": "2", "name": "Ashish"}]
list2 = [{'id': "1", 'age': 20}, {'id': "2", 'age': 21}]
list3 =[{'id': "1", 'addre': "Nagpur"}, {'id': "2", 'addre': "pune"}]
list4 = []
for i in range(len(list1)):
    dict = {}
    if list1[i]['id'] == list2[i]['id'] == list3[i]['id']:
        dict.update(list1[i])
        print(dict)
        dict.update(list2[i])
        print(dict)
        dict.update(list3[i])
        print(dict)
        list4.append(dict)
print(list4)

dict = {'a':1, 'b': 2, "c":3, "d" : 4}
dict_2 = {k:v*2 for (k,v) in dict.items()}
print(dict_2)

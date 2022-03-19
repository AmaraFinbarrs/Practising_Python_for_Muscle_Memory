# How to create a dictionary in Python.
# An Article by DIONYSIA LEMONAKI on freeCodeCamp Website.
# I used this to reinforce my knowledge of dictionaries in python
# I suggest you read the article too

# {} or built-in dict() function

# First to create an empty dictionary
my_dictionary = {}
print('my_dictionary:', my_dictionary)

# create a dictionary
my_information1 = {'name': 'Dionysia', 'age': 28, 'location': 'Athens'}
print('my_information1:', my_information1)
# check data type
print(type(my_information1))

# create a dictionary with dict()
my_information2 = dict({'name': 'Dionysia', 'age': 28, 'location': 'Athens'})
print(('my_information2:', my_information2))
# check my data type
print(type(my_information2))

# create a dictionary using the dict.fromkeys function
info_needed = ['name', 'age', 'location']
info_provided = ['Dionysia', 28, 'Athens']
for count, info in enumerate(info_provided):
    information = dict.fromkeys(info_needed, info_provided[count])
print('Information:', information)

# creating a dictionary using fromkeys() without setting a value for all the keys
# create a sequence of string
cities = ('Paris', 'Athens', 'Madrid')
# create the dictionary, 'my_dictionary' using the fromkeys() method
my_dictionary = dict.fromkeys(cities)
print('my_dictionary with keys:', my_dictionary)

# Another example that sets the same values for all the keys in the dictionary
# use the same sequence of strings 'cities' above
# create a single value
continent = 'Europe'
my_dictionary = dict.fromkeys(cities, continent)
print('my_dictionary with all the same values', my_dictionary)

# lets we have the following
my_dictionary = {True: 'True', 1: 1, 1.1: 1.1, 'one': 1, 'languages': ['Python']}
print(my_dictionary)

# HOW TO FIND THE NUMBER OF key-value PAIRS CONTAINED IN A DICTIONARY IN PYTHON.

# len() returns the value of key-value pairs enclosed in the dictionary
print(''' ''')
print(len(my_information2))

# HOW TO view all key-value pairs contained in a Dictionary in Python using item() method
print(my_information2)  # returns the dictionary itself
print(my_information2.items())  # returns a list of tuples that contains the key-value pairs inside the dictionary

# HOW TO VIEW ALL key-value PAIRS CONTAINED IN A DICTIONARY IN PYTHON
# To do this we use the built-in keys() method:
years_of_creation = {'Python': 1993, 'JavaScript': 1995, 'HTML': 1993}
print(years_of_creation.keys())

# HOW TO VIEW ALL values CONTAINED IN A DICTIONARY IN PYTHON
# To do this we use the built-in values()method
print(years_of_creation.values())

# HOW TO ACCESS INDIVIDUAL ITEMS IN A DICTIONARY IN PYTHON
my_information = {'name': 'Dionysia', 'age': 28, 'location': 'Athens', 1: 'Number one'}
print(my_information[1])
# print(my_information['job']) would return a KeyError because the key is not in the dictionary
# one way to avoid this from happening is to first search to see if the key
# is in the dictionary in the first place

print('job' in my_information)  # False
print('name' in my_information.values())  # False
print('28' in my_information.keys())  # False

# Another way to get access in the dictionary is by using the get() method
print(my_information.get('job'))  # Returns None instead of an KeyError message
# with this get(), instead of showing None value, you can customise ir by providing a different value
print(my_information.get('Job', 'This value does not exist'))

print(''' 

''')

# HOW TO MODIFY A DICTIONARY IN PYTHON
# Dictionaries can grow and shrink in size
new_dictionary = {}
print(new_dictionary)

# Add a new item
new_dictionary['name'] = 'John Doe'
new_dictionary['age'] = 34
new_dictionary['age'] = 100  # replacing the previous key with same name because keys are unique
print(new_dictionary)

# to update a dictionary, you can also use the built-in() method
# particularly helpful when you want to update more than one value.
new_dictionary.update(name='Amanda', age=25, occupation='Software Engineer')
print(new_dictionary)

numbers = {'one': 1, 'two': 2, 'three': 3}
print('numbers: ', numbers)
more_number = {'four': 4, 'five': 5, 'six': 6}
print('more_number: ', more_number)
numbers.update(more_number)
print('numbers updated with more numbers: ', numbers)

print(''' 

''')

# HOW TO DELETE ITEMS FROM A DICTIONARY IN PYTHON
# one way is to use the del keyword
my_information = {'name': 'Dionysia', 'age': 28, 'location': 'Athens'}
del my_information['location']
print(my_information)

# if you want to remove a key but also save that removed value, use the built-in pop() method
my_information = {'name': 'Dionysia', 'age': 28, 'location': 'Athens'}
city = my_information.pop('location')
print(my_information)
print(city)
# if you specify a key that does not exist in the dictionary, you will get a KeyError error message
Friend = my_information.pop('friend_name', 'Not Found')
print(Friend)

# the pop() method removes a specific key and its assocaited value - but what if you only
# delete the last key-value pair from a dictionary
# to do that, we use the built-in popitem method instead
popped_item = my_information.popitem()
print(popped_item)

# if you want to delete the all key-value pairs from a dictionary, use the built-in function clear() method
my_information = {'name': 'Dionysia', 'age': 28, 'location': 'Athens'}
my_information.clear()
print(my_information)
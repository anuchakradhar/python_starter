# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#create dict
person = {
    'first_name' : 'Anu',
    'last_name' : 'Chakradhar',
    'age' : 24
}

#get value of dict
print(person['first_name'])
print(person.get('last_name'))

#add value
person['phone'] = 1234456789

#get dict key
print(person.keys())

#get dict items
print(person.items())

#copy a dict
person2 = person.copy()
person2['address'] = 'Bhaktapur'

print(person2)

#remove from dict
del(person['age'])
person.pop('phone')

#clear
#person.clear()

#get length
print(len(person2))

print(person)

#List of dict
person2 = [

    {'name': 'Sanu', 'age': 20},
    {'name': 'Tanu', 'age': 39}
]

print(person2[1]['name'])
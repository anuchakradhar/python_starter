# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#create tuple
fruits = ('Apple', 'Oranges', 'Mangoes')

#Cannot change value of tuple
fruits[1] = 'Pears'

#delete tuples
del fruits


#Length of fruits
print(fruits)
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
#Create set
fruits_set = {'Apple', 'Orange', 'Mango'}

#check in set
print('Apple' in fruits_set)

#Add in set
fruits_set.add('Grapes')

#remove in set
fruits_set.remove('Mango')

#clear the set
fruits_set.clear()

#delete the set
del fruits_set

print(fruits_set)
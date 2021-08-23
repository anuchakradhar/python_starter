# A List is a collection which is ordered and changeable. Allows duplicate members.


number = [1, 2, 3, 4, 5]
fruits = ['Mango', 'Apple', 'Grapes','Strawberry']



print(number)

#Length of list
print(len(fruits))

#Get a value
print(fruits[1])

#change value
fruits[1] = 'Pears'

#Last value
print(fruits[-1])

#append the value
fruits.append('Banana')

#remove the value
fruits.remove('Grapes')

#remove with pop
fruits.pop(2)

#insert into position
fruits.insert(1, 'Lichi')

#reverse
fruits.reverse()

#sort
fruits.sort()

#reverse sort
fruits.sort(reverse=True)

print(fruits)

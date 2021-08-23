# Python has functions for creating, reading, updating, and deleting files.

#open a file
myFile = open('myFile.txt', 'w')

#Getting some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

#write in file
myFile.write('I love Python ')
myFile.close()

#Append to file
myFile = open('myFile.txt', 'a')
myFile.write('and my name is Anu')
myFile.close()


#Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(50)
print(text)

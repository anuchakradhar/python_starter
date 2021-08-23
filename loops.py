# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
numbers = [1, 2, 3, 4, 5]
# simple for loop
for num in numbers:
    print(f'current number: {num}')

# #break
for num in numbers:
    if num==3:
        break
    print(f'current number: {num}')

# #continue
for num in numbers:
    if num==3:
        continue
    print(f'current number: {num}')

#range
for i in range(len(numbers)):
    print(numbers[i])

for i in range(10):
    print (i)

# While loops execute a set of statements as long as a condition is true.
count = 0
while count <=10:
    print (count)
    count += 1
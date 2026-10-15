"""
lists are 
- ordered
- changeable 
- use square brackets

note: python starts counting from zero

"""

numbers = [1, 2, 3, 4]
print(numbers)

fruits = ['apple', 'cherries', 'bananas']
print(fruits)

mixed = ['hello', 5, True, None]
print(mixed)

#access items in a list

print(numbers[0])
#prints the first item in the list, numbers
#can do negative indexing [-1] would print the last element in the list

fruits[0] = "grape"
print(fruits)
#changes first element to something different

#adding items to end of list
numbers.append(6)
print(numbers)

#adding items to anywhere in the list
print(mixed.insert(1, False))
print(mixed)

#remove items from a list
fruits.remove("bananas")
print(fruits)

#or

fruits.pop(0)
print(fruits)

#for loop to see everything in the list
for num in numbers: 
    print(num)

#slicing (grab a portion of the list)
slicing_nums = numbers[1:4]
print(slicing_nums)

#striding (grab a portion of the list in pattern format)
stridiing_num = numbers[::1]
print(stridiing_num)
str_nums = numbers[1:8:2] #[start:stop:step]
print(str_nums)

print(numbers[:3]) #doesn't include 40 bc it's exclusive 
'''
1 .append() adds an element to the end of the list
2 .extend() appends the element of another list to the end of the current list
3 .insert() Inserts an element at a specified position in the list.
4 .remove() Removes the first occurrence of a specified value from the list.
5 .pop() Removes and returns the element at the specified index (default is the last
element).
6 .clear() Removes all elements from the list.
7 .index() Returns the index of the first occurrence of a specified value.
8 .count() Returns the number of occurrences of a specified value in the list.
9 .sort() Sorts the elements of the list in ascending order
10 .reverse() Reverses the order of the elements in the list.
11 .copy() Returns a shallow copy of the list.

'''

#dictionaries (assigning a key to a value)

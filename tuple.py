# thistuple = ("apple", "mango","banana", "kiwi")
# print(thistuple)

# Example
# Tuples allow duplicate values:
# thistuple = ("apple", "mango","banana", "kiwi", "apple", "mango","banana", "kiwi")
# print(thistuple)

# Example
# Print the number of items in the tuple:
# thistuple = ("apple", "banana", "mango", "kiwi")
# print(len(thistuple))

# Chat Gpt: count:
# my_tuple =(1,2,3,2,2,4)
# print(my_tuple.count(2))

# index:
# my_tuple = (1,2,3,2,4)
# print(my_tuple.index(2))
# print(my_tuple.index(2,2))

# Example:
# Print the second item in the tuple:
# thistuple = ("apple", "mango", "banana", "kiwi")
# print(thistuple[3])

# Negative indexes:
# Example
# Print the last item of the tuple:
# thistuple = ("apple", "mango", "banana")
# print(thistuple[-1])

# Range of Index:
# Example: Return the third, fourth, and fifth item:
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[3:6])

# Example
# This example returns the items from the beginning to, but NOT included, "kiwi":
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# Example
# This example returns the items from "cherry" and to the end:
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[3:])

# Range of Negative index:
# Example
# This example returns the items from index -4 (included) to index -1 (excluded)
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# Example
# Check if "apple" is present in the tuple:
# thistuple = ("apple", "banana", "cherry")
# if "banana" in thistuple:
#     print("yes, 'banana' is in tuple fruit")


# Example
# Convert the tuple into a list to be able to change it:
# x = ("apple", "mango", "banana")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# convert into list:
# Example:
# Convert the tuple into a list, add "orange", and convert it back into a tuple:
# thistuple = ("apple", "mango", "banana", "kiwi")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y) 
# print(thistuple)

# add tuple to a tuple:
# Example:
# Create a new tuple with the value "orange", and add that tuple:
# thistuple = ("apple", "banana", "mango", "orange")
# y = ("kiwi",)
# thistuple += y
# print(thistuple)

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
# thistuple = ("apple", "banana", "kiwi", "orange")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

# The del keyword can delete the tuple completely:
# thistuple = ("apple", "mango", "banana", "orange")
# del thistuple
# print(thistuple)

# packing Tuple:
# fruit = ("apple", "banana", "kiwi")
# print(fruit)

# Unpacking tuple:
# fruit = ("apple","mango", "orange")
# (green, yellow, blue) = fruit
# print(yellow)
# print(green)
# print(blue)

# Assign the rest of the values as a list called "red":
# fruit = ("apple", "mango", "orange","pineapple", "pomegrante")
# (green, *red, yellow) = fruit
# print(green)
# print(red)
# print(yellow)


# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)

# loops tuples: for loop:
# Iterate through the items and print the values:
# thistuple = ("apple", "mango", "banana")
# for x in thistuple:
#     print(x)

# Print all items by referring to their index number:
# thistuple = ("apple", "mango", "banana", "orange")
# for i in range(len(thistuple)):
#     print(thistuple[i])

# using while loop:
# Print all items, using a while loop to go through all the index numbers:
# thistuple = ("mango", "orange", "apple", "papaya")
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = i+1

# join tuples: join two tuples:
# tuple1 =("a", "b", "c")
# tuple2 =("1", "2", "3")
# tuple3 = tuple1+tuple2
# print(tuple3)

# Multiply tuples:
# Multiply the fruits tuple by 2:
# fruits = ("mango", "orange", "apple")
# mytuple = fruits * 3
# print(mytuple)











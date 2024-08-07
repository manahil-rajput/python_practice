# Example 1: (Break)
# Q:Exit the loop when i is 3:
# i = 1
# while i < 6:
#   print(i)
#   if (i == 3):
#     break
#   i += 1



# Example 2: (Continue)
# Q: Continue to the next iteration if i is 3:

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i = 1
# while i <= 10:
#   if(i%2 == 0):
#    i += 1
#    continue #skip
#   print(i)
#   i += 1

# Exit the loop when x is "banana":

# fruit = ["Mango", "banana", "kiwi", "guava", "cheery"]
# for x in fruit:
#     print(x)
#     if x == "kiwi":
#         break
    
# Example:
# Exit the loop when x is "banana", but this time the break comes before the print:

# fruit = ["Mango", "banana", "kiwi", "guava", "cheery"]
# for x in fruit:
#     if x == "kiwi":
#       break
#     print(x)

# Example
# Do not print banana:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# Example
# Print all numbers from 0 to 5, and print a message when the loop has ended:

# for x in range(6):
#     print(x)
# else:
#     print("finally finished!")

# Example
# Break the loop when x is 3, and see what happens with the else block:

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")




# while True:
#     print("hello") is condition main hello print hi hota rahy ga. Ruky ga nahi. isi liye hm kahin na kahin asi value b lain gy ky yeh value false b hojy wrna true main to o chalta hi rahy ga. isi liye hm ak count ka variable bnaty hai.

# count = 1
# while count <= 5 :
#     print("hello")
#     #count = count + 1 is trhan b likh sakty hain increase kr sakty haior nichy jasy diya wasy b.
#     count += 1
# print(count)

# print numbers from 1 to 5
# i = 1
# while i <= 50000:
#     #print("Manahil" , i)
#     print(i)
#     i+=1
#     print("Loop ended")

# i = 5
# while i >= 1:
#     print("Manahil" , i)
#     print(i)
#     i-=1
     
#     print("Loop ended")

# i = 5
# while i < 6:
#     print(i)
#     i -= 1
#     print("Loop ended") yeh infinite hai chalta  rahy ga.

# Practice Question:

#  Q#1: Print numbers from 1 to 100.

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# Q#2: Print numbers from 100 to 1.
# i = 100
# while i >= 1: #stopping Condition.
#     print(i)
#     i -= 1

# Q#3: Print the multiplication table of a number n. n hm kuch b ly sakty hain jis ka hm ny tableprint karwana hota hai 
# i = 1
# while i <= 10:
#     print(4*i)
#     i += 1
    #<------------------------------->
# n = int(input("enter the number : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1


# Q#4: Print the elements of the following list using a loop.
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# heroes = ["ironman", "thor", "superman" , "batman"]

# traverse
# i = 0 
# while i < len(heroes):
#    print(heroes[i])
#    i += 1


# idx = 0 
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1
    #<------------------------>
# idx = 0
# while idx < len(nums):
#     print(nums[idx]) #nums[0], nums[1], nums[2].......
#     idx += 1


# Q#5: Search for a number x in this tuple using loop:
#  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# x = 36
# i = 0   #initialization
# while i < len(nums):
#    if(nums[i] == x):
#     print("FOUND at idx", i)
#    else:
#     print("finding..")
#     i += 1

#W3school:
# Print i as long as i is less than 6:
# i = 1
# while i < 6:
#   print(i)
#   i += 1



# Else Statment:
# Print a message once the condition is false

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")


# let's Practice: 
# Question: what a program to find the sum of the first n numbers.(using while)


#  n = 7
# sum = 0
# i = 1
# while i <= n:
#     sum +=i
#     i +=1
#     print("total sum =", sum)


# Question: what a program to find the factorial of first n numbers.(using while)

# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i +=1
# print("factorial =", fact)

# loop list:
# Print all items, using a while loop to go through all the index numbers.

# thislist = ["apple", "mango", "banana"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i+1 

# Example
# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "mango"]
[print(x) for x in thislist]



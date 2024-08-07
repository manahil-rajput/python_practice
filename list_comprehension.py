# marks = [20, 30, 40, 50, 60]
# new_marks = []
# for x in marks:
#     new_marks.append(x+2)
#     print(new_marks)
# OR   yeh do treeky hain uor ala code 5 lines ka tha nichy wala 3 to nichy waly k list comprehension kahty hain. 
# marks = [20, 30, 40, 50 ,60]
# new_marks = [x+2 for x in marks]
# print(new_marks)

# cube = []
# for x in range(10):
#     if x % 2 == 0:
#         cube.append(x**3)
#         print("using for loop:", cube)
#  OR:
easy = [x ** 3 for x in range(10) 
        if x % 2 == 0]
print("using list comprehension:" , easy)
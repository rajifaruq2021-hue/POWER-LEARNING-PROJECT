# 1.I have to firrstly create an empty list called my_list.
my_list = []
print(f"Initial empty list: {my_list}")

# 2. Then I will append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending elements: {my_list}")

# 3. Next is to insert the value 15 at the second position in the list.
# We have to now that in Python, list indices start at 0, so the second position is index 1.
my_list.insert(1, 15)
print(f"After inserting 15 at the second position: {my_list}")

# 4. Next is to extend my_list with another list: [50, 60, 70].
extension_list = [50, 60, 70]
my_list.extend(extension_list)
print(f"After extending with [50, 60, 70]: {my_list}")

# 5. Then I will have to remove the last element from my_list.
my_list.pop()
print(f"After removing the last element: {my_list}")

# 6. Next stage is to sort my_list in ascending order.
my_list.sort()
print(f"After sorting in ascending order: {my_list}")

# 7. Finally I will have to find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30) 
print(f"The index of the value 30 is: {index_of_30}")
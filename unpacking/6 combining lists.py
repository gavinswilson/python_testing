list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(*list1)
print(f"Combined List: {combined}\n")


# why not

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in list2:
    list1.append(item)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]
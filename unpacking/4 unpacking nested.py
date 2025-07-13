data = ("gav", (35, "Eng"))

a, (b, c) = data

print(a, b, c)  # Output: gav 35 Eng


# vs

nested_list = [1, 2, ['a', 'b', ['x', 'y']], 3]
# To access the element 2.


element = nested_list[1]
    # element will be 2
# To access the inner list ['a', 'b', ['x', 'y']]:
# Python

inner_list = nested_list[2]
    # inner_list will be ['a', 'b', ['x', 'y']]
# To access the element 'a' within the first inner list:
# Python

char_a = nested_list[2][0]
    # char_a will be 'a'
# To access the innermost list ['x', 'y']:
# Python

innermost_list = nested_list[2][2]
    # innermost_list will be ['x', 'y']
# To access the element 'x' within the innermost list:
# Python

char_x = nested_list[2][2][0]
    # char_x will be 'x'
# Modifying Elements:
# You can also modify elements in a nested list by referencing them with multiple indices and assigning a new value:
# Python

nested_list[2][1] = 'c'
# nested_list will become [1, 2, ['a', 'c', ['x', 'y']], 3]
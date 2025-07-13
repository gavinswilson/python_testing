dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined_dict = {**dict1, **dict2}
print(f"Combined Dictionary: {combined_dict}\n")


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2
print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4}


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)
# Output: {'a': 1, 'b': 3, 'c': 4}


from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined_map = ChainMap(dict1, dict2)
print(combined_map)
# Output: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
print(combined_map['b'])
# Output: 3 (from dict2, as it's listed first in ChainMap)

# The union operator (|) and dictionary unpacking (**) are generally preferred for creating new merged dictionaries due to their conciseness.
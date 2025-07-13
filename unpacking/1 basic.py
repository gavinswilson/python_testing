# basic unpacking example
# works with tuples, lists, and other iterables (strings)
a,b,c = [1, 2, 3]

d,e,f = ("bob", 6, True)
g,h,i = d
print(a, b, c)  # Output: 1 2 3
print(d, e, f)  # Output: bob 6 True
print(g, h, i)  # Output: b o b



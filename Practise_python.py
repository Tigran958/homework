from colections import counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
b = {}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
print(len(d1))
a = counter(d1) + counter(d2)
print(a)
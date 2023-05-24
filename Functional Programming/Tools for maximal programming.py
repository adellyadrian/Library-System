# zip
a = [1, 2, 3, 4]
b = ["Adam", "Jack", "Bob"]
c = [24, 42, 12]


for index, name, grade in zip(a, b, c):
    print(index, name, grade)

# map


def foo(x):
    return x**2


a = [12, 24, 42]

# Option 1.1
for element in a:
    print(foo(element))

# Option 1.2
for i in range(len(a)):
    print(foo(a[i]))

# Option 2
for i in map(foo, a):
    print(i)

# enumerate

a = ["Adam", "Jack", "Bob"]

for index, name in enumerate(a, start=1):
    print(index, name)


# filter
a = [67, 24, 56, 0, 23, 57, 89, 44, 91]


def foo(x):
    return x % 2


for i in filter(foo, a):
    print(i)

for i in a:
    if foo(i):
        print(i)

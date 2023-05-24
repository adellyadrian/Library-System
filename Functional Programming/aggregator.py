# Crate a function `aggregator`
# Input: 1 or more collections
# Output: a list with sums of according elements from all the lists


def aggregator(*args):
    result = []
    for e in zip(*args):
        result.append(sum(e))
    return result


# Test 1
l_1 = [12, 24, 42]
res = aggregator(l_1)
print(res)
assert res == [12, 24, 42]

print("==========")

# Test 2
l_1 = [12, 24, 42]
l_2 = [1, 2, 3, 4, 5, 6]
l_3 = [0, 1, 0, 1]
res = aggregator(l_1, l_2, l_3)
print(res)
assert res == [13, 27, 45]

set = {20,76,528,8970,7,7}

print(set)


set.add(0)

print(set)

set.remove(528)

print(set)

#operations on sets

set1 = {75,6237,8364,52,74}

set2 = {1,74,7,75,859,10,54}

set3 = {75,52,74}

print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))

print(set2.difference(set1))

print(set1.symmetric_difference(set2))

print(set3.issubset(set1))

print(set1.issuperset(set3))

print(set3.issubset(set2))

print(set3.isdisjoint(set))

print(set1.intersection_update(set2))

print(set1)
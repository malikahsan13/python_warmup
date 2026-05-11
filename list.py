friends = ["abc", "def", "eif", "Toy", "ref"]

lucky_numbers = [1, 2, 3, 4, 5, 6, 7]

print(friends[0])

print(friends[1:])

print(friends[-1])  # last element

friends.extend(lucky_numbers)

friends.append(lucky_numbers)

friends.insert(1, "Ali")

friends.remove("Ali")

# friends.clear()

friends.pop()

print(friends.index("abc"))

print(friends.count("abc"))

lucky_numbers.sort()

lucky_numbers.reverse()

friends2 = friends.copy()

print(len(friends))

print(friends)

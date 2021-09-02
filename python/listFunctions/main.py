lucky_numbers = [7, 13, 21]
buddies = ["Jesse", "Nikki", "Victor"]

print(buddies)

buddies.extend(lucky_numbers)

print(buddies)

buddies.append("Milo")

print(buddies)

buddies.remove("Milo")
buddies.insert(3, "Milo")
buddies.append(39)

print(buddies)

buddies.pop()

print(buddies)
print(buddies.index("Victor"))
print(lucky_numbers.count(7))

lucky_numbers.reverse()

print(lucky_numbers)

lucky_numbers.sort()

print(lucky_numbers)

buddies.clear()

print(buddies)

buddies = lucky_numbers.copy()

print(buddies)

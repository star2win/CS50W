from functions import square, Point

#name = input()
name = "Filip"
print(f"Hello, {name}!")

for i in range(5):
    print(i)

names = ["Alice", "Bob", "Charlie"]
for i in names:
    print(i)

s = set()
s.add(1)
s.add(3)
s.add(5)
print(s)

ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30
ages["Alice"] += 1
print(ages)

for i in range(10):
    print(f"{i} squared is {square(i)}")

print(square(10))

p = Point(3, 5)
print(p.x)
print(p.y)


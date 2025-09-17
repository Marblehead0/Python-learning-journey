numbers = [1,2,3,4,5]
squares = [n**2 for n in numbers]

print(squares)

names = ["Anthony","Alfred","Chris","Bobby","Nikita"]
newNames = [n for n in names if n.startswith("A")]

print(newNames)
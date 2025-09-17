def greet(name):
    return f"hello, {name}!"

print(greet("Chris"))
print(greet("Fred"))

def add_numbers(a,b):
    return str(int(a) + int(b))

print(add_numbers(1,2))

def is_even(n):
    if(n%2 == 0):
        return "Even"
    else:
        return "Uneven"

print(is_even(1))
print(is_even(10))
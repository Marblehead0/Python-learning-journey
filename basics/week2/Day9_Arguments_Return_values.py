def power(base,exponent=2):
    return base ** exponent

print(power(3))
print(power(3,3))

def introduce(name,age):
    print(f"My name is {name} and i am {age} years old")

introduce(age = 29,name="Chris")

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

print(convert_to_celsius(98.6))

def convert_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

print(convert_to_fahrenheit(37))
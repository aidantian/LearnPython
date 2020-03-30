# 1 Comment Hellow World

i = 1
print("Hello World")
print("o---")
print("  ||||")
print("*" * 10)
print("-" * 80+"\n")
print("-" * 30 + str(i) + " Comments" + "-" * 30)
i += 1

# 2 Variable
price = 10
price = 20
rating = 4.9
name = "Tommy"
is_published = False

name = "Tommy"
color = "Red"
'''
name = input("what's your name? ")
color = input("What is your favorite color? ")
'''

print(name + " Like " + color)
print("-" * 30 + str(i) + " Comments" + "-" * 30)
i += 1

# 3 Comments
birth_year = 1976
# birth_year = input("Birth Year: ")
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))

print(age)
print("-" * 30 + str(i) + " Comments" + "-" * 30)
i += 1

# 4 Comments
weight_lbs = 152
# weight_lbs = input("Weight (lbs): ")
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)

print("-" * 30 + str(i) + " Comments" + "-" * 30)
i += 1

# 5 Comments
course = 'Python for "Beginners"'
print(course)
print(course[-1])
print(course[0:5])
print(course[0:])
print(course[:5])
print(course[:])
print(course[1:-1])
course = '''
Hi This is multiple lines

This is Tommy Tian

'''
print(course)

print("-" * 30 + str(i) + " Comments" + "-" * 30)
i += 1

# 6 Comments
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

course = 'Python for Beginners'
print(len(course))


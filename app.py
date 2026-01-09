import math
Students_count = 2000
print("Total number of students:", Students_count)
rating = 4.99
is_published = True
course_name = "Python Programming"

print("Course Name:", course_name)
print("Course Rating:", rating)
print("Is the course published?", is_published)
print("Data Types:")
print(len(course_name))
print(course_name[0])
print(course_name[2])
print(course_name[-1])
print(course_name[0:5])
print(course_name[0:])
print(course_name[:6])
print(course_name[:])
course = "Python \"Programming"
print(course)
course = "Python \Programming"
print(course)
course = "Python \nProgramming"
print(course)
first_name = "Abubakar"
last_name = "Bello"
full_name = first_name + " " + last_name
print(full_name)
full_name = f"{first_name}{last_name}"
print(full_name)

full_name = f"{len(first_name)} {last_name}"
print(full_name)


full_name = f"{len(first_name)} {3 + 3}"
print(full_name)

course = "  Python Programming"
print(course.upper())

course_capital = course.upper()
print("Capitalized Course:", course_capital)

course_small = course.lower()
print("Small Course:", course_small)

print("Title Case Course:", course.title())


print("Stripped Course:", course.strip())
print("Position of 'Pro':", course.find("Pro"))

course_replace = course.replace("P", "J")
print("Replaced Course:", course_replace)

print("Pro" in course)

print("Java" not in course)
print("Pro" not in course)


# Arithmetic Operations
x = 1
x = 1.1
x = 1 + 2j  # a + bi

print(3+5)
print(10 - 2)
print(4 * 2)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 4)

print(round(2.9))

print(abs(-2.9))

print(math.ceil(2.2))

# Input Function
# x = input("x: ")
# y = (int(x)) + 1
# print(f"x: {x}, y: {y}")
# int(x)
# float(x)
# bool(x)
# str(x)

# falsy_values = [0, 0.0, "", None, False]
# truthy_values = [1, -1, 0.1, "abc", True, [1, 2, 3]]

a = bool(0)  # False
print(a)
b = bool("abc")  # True
print(b)
c = bool("")  # False
print(c)
bool(1)  # True
d = bool(1)  # True
print(d)
bool(-1)  # True
e = bool(-1)  # True
print(e)
f = bool("false")  # True
print(f)


# comparison operators
10 == 10  # True
10 != 5  # True
10 > 5  # True
10 < 20  # True
2 > 10  # False
5 <= 5  # True
5 >= 10  # False
10 >= 5  # True
10 == "10"  # False
10 != "10"  # True
10 != 10.0  # False
10 != 5.0  # True
"bag" > "apple"  # True
"bag" < "apple"  # False
"bag" == "BAG"  # False

# Conditional Statement
temperature = 5
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's a cold day")
print("Enjoy your day")

# Ternary Operator
# age = 16
# if age >= 18:
#    print("You are eligible for admission")
# else:
#    print("You are not eligible for admission")

# age = 19
# if age >= 18:
#     message = "You are eligible for admission"
# else:
#     message = "You are not eligible for admission"
# print(message)

# age = 12
# message = "You are eligible for admission" if age >= 18 else "You are not eligible for admission"
# print(message)

# logical operators
high_income = True
good_credit = True
student = True
# if high_income and good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")
# if high_income or good_credit:
#     print("Eligible for loan")
# if not student:
#     print("Eligible for loan")
# else:
#     print("Student are Not eligible for loan")

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# SHORT CIRCUIT EVALUATION
if high_income or good_credit or not student:
    print("Eligible for loan of $10,000")

age = 22
# if age >= 18 and age <= 65:
if 18 <= age <= 65:
    print("You are Eligible")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

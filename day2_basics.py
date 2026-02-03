age = 25
height = 5.9
name = "Tejinder"
is_driver = True

print(age)
print(height)
print(name)
print(is_driver)

age = input("What is your age?")
print("Hello", name)
print("You are ", age, " years old")

age = input("Enter your age: ")
age = int(age)
future_age = age + 10

print("In 10 years, you will be ", future_age, " years old")

name = input("Enter your name: ")
hours = input("How many hours do you drive Uber per day? ")
hours = int(float(hours))

if hours >= 8:
    print(name, " You are working very hard. Respect")
else:
    print(name, " You have room to grow. Keep pushing")

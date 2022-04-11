name = input("What is your name? ")
colour = input("What is your favourite colour? ")
print(name + " likes the colour " + colour)

birth_year = input("What year were you born in? ")
age = 2020 - int(birth_year)
print("You are " + age.__str__() + " years old")

weight_lbs = input("How much do you weigh in pounds? ")
weight_kg = int(weight_lbs) / 2.205
print("You weigh " + weight_kg.__str__())
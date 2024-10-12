# input() function will always return a string. Use type conversion to manipulate the stored value.
# int()
# float()
# str()
# bool()

birth_year = input("Enter your birth year: ")
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)

# program to ask user weight in lbs and convert to kgs

print("----------------------------------------")
print("--------- Weight Converter -------------")
print("----------------------------------------")
weight = input("Enter your weight in LBS: ")
print(type(weight))
converted_weight = int(weight) / 2.2046
print("Calculating your weight in KGS ...")
print("Your weight converted is " + str(converted_weight) + " KGS.")
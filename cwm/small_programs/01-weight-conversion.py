print("-----------------------------------")
print("------- Weight Conversion ---------")
print("-----------------------------------")

unit = input("Choose (K)gs or (L)bs: ")
weight = input("Enter your weight: ")

# Now we want to ensure that measure is set to one of upper or lower for consistency

adjusted_unit = unit.upper()

# if statement now we have sanitized the inputs

if adjusted_unit == "K":
    sum = int(int(weight) * 2.2046)
    print(f"Your weight converted to pounds is {sum}.")
elif adjusted_unit == "L":
    sum = int(int(weight) / 2.2046)
    print(f"Your weight converted to kilograms is {sum}.")
else:
    print("You entered an invalid value for (K)gs or (L)bs")
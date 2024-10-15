is_light = False
is_dark = False

if is_light:
    print("The sun is up, it's a beautiful day")
elif is_dark:
    print("It's night time, go to sleep Maisie")
else:
    print("We have reached a new phase where light and dark no longer exist.")


print("-----------------------------------")
print("------- Downpayment Model ---------")
print("-----------------------------------")

house_price = 1000000
good_credit = False
good_downpayment = int(house_price * 0.1)
poor_downpayment = int(house_price * 0.2)

if good_credit:
    print("You have been assessed as having good credit")
    print("Your downpayment is $" + str(good_downpayment))
else:
    print("You have been assessed as having poor credit")
    print("Your downpayment is $" + str(poor_downpayment))

# Using the logical AND operator. Build an example to assess is an applicant is suitable for a loan based on
# two values, high_income and good_credit. Switch 'and' to 'or' operator to match on at lease one value

print("-----------------------------------")
print("--------- Loan Assessment ---------")
print("-----------------------------------")

high_income = True
good_credit = False

if high_income and good_credit:
    print("Loan application was successful")
else:
    print("Loan application was denied")

# The 'not' operator asseses an unmatched value positively. For example a False bool will match. In the
# below example we want to treat a False bool positively

good_credit = True
criminal_record = True

if good_credit and not criminal_record:
    print("Loan application was accepted as you aren't a criminal")
else:
    print("Loan application was denied as you are a criminal")


# Use comparison operators to compare a variable with a value rather than a Boolean
# == equal to (the equality operator)
# != not equal to
# < > less than and more than
# <= >= less than or equal and more than or equal

print("-----------------------------------")
print("--------- Weather Notice ----------")
print("-----------------------------------")

celcius = 19

if celcius >= 26:
    print(f"It's a hot one at {celcius} degrees. Drink lots of water.")
elif celcius == 23:
    print(f"Wow, {celcius} degrees. My favorite temperature.")
elif celcius <= 15:
    print(f"It's {celcius} degrees and chilly today. Wrap up warm.")
else:
    print(f"The day is pleasant enough at {celcius} degrees.")

# Create an input for the user. Ensure the inout length is at least 3 char and no more than 50 char.
# Assess the input and return the appropriate message to the user

print("-----------------------------------")
print("------- Char length assess --------")
print("-----------------------------------")

username = input("Enter your desired username: ")
char_length = len(username)
print(char_length)

if char_length < 3:
    print(f"The username: '{username}' is too short, please run the program again.")
elif char_length > 30:
    print(f"The username: '{username}' is too long, please run the program again. ")
else:
    print(f"'{username}' is a great choice. Let's continue.")

# extracting a single character from a string - remember, python is zero-indexed
str1 = "educational"
print(str1[4])

# python can use negative index to print characters from the end of the string
print(str1[-1])

# a start and end point of the index for extracting chars can also be defined either side of :
print(str1[1:-6]) # will return "duca"

# Formatted strings can be used to set placeholders and make the string more readable
first_name = "Alfred"
second_name = "X"
message = first_name + ' [' + second_name + '] is a coder' # Inefficient - use formatted string
print(message)

formatted_message = f"{first_name} [{second_name}] is a coder" # Easier to interpret
print(formatted_message)

# String methods are components features to a string, like upper and lower case
str2 = "A string to be manipulated"
print(len(str2)) # <--- prints the length of the string using the len() function

print(str2.upper()) # <--- Using the string method "upper"

print(str2.lower())

print(str2.find("i")) # <--- Finds the index position in the string of the first instance of the char "i"

str2_replace = str2.replace("manipulated", "messed with") # <--- replace one string value with another
print(str2_replace)
print(str2_replace.upper())

print("man" in str2) # <--- Returns a boolean value (in this case True). 'in' is an operator not a method
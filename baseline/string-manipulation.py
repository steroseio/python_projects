# extracting a single character from a string - remember, python is zero-indexed
str1 = "educational"
print(str1[4])

# continuous sections of one or more characters are known as substrings

print("---------------------------------------------------")
print("l e a r n i n g   <------- string")
print("0 1 2 3 4 5 6 7   <------- index")
print("  e a r n         <------- substring")
print("  1 2 3 4 5       <------- 1 = starting index, 5 = ending index")

print("---------------------------------------------------")
print("---------------------------------------------------")

word = "learning"
print(word[1:5])

# slicing is the extraction of part of a string, list or tuple, as below
str1 = "scrumptious"
i = 1
j = 6
str2 = str1[i:j]
print(str2)

# Can leave out the ending index to slice the string
str1 = "Unequivocal"
str2 = str1[2:]
print(str2)

# similarly, leave out the starting index
str1 = "Goldfish"
str2 = str1[:4]
print(str2)

# manipulate a string by swapping out words
sentence = "I like rocks but they seem indifferent."
conjunction_index = sentence.find("but")
print(conjunction_index)
left_side = sentence[0:conjunction_index]
print(left_side)
right_side = sentence[conjunction_index + 3:]
print(right_side)
classy_sentence = left_side + "yet" + right_side
print(classy_sentence)

print("---------------------------------------------------")
print("---------------------------------------------------")

# The 'replace' function returns a new string in which all instances of one substring
# are replaced with another substring.
forecast = "It will be rainy today."
new_forecast = forecast.replace("rainy", "sunny")
print(forecast)
print(new_forecast)
forecast_more = new_forecast.replace("today", "tomorrow")
print(forecast_more)

# replace output can be embedded in a different function rather than assigned to a
# new variable. But doing this means it cannot be re-used.
words = "red shirt"
words.replace("red", "blue")
print(words)
print(words.replace("red", "blue"))
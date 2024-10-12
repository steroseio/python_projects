# A look at the basic arithmetic operators available in Python
print(10 + 3) # <--- Addition

print(10 - 3) # <--- Subtraction

print (10 * 3) # <--- Multiplication

print(10 ** 3) # <--- Power (10 * 10 * 10)

print (10 / 3) # <--- Division to float

print(10 // 3) # <--- Division to integer

print (10 % 3) # <--- Modulus (integer remainder after division)

# To increment a number and store the increment as a variable we could use the following
x = 10
x = x + 3
print(x)

# An augmented assignment operator can produce this more efficiently
x += 3
print(x) # <--- Remember x is already 13 due to the increment above, so this produces 13 + 3 = 16

x -= 10
print(x)

# Operator precedence - a basic math operation, power (exponation) precedes multiplication and division, 
# precedes addtion and subtraction

y = 10 + 3 * 3 ** 3 # <--- 91 as 3 ** 3 = 27, 27 * 3 = 81, 81 + 10 = 91
print(y)

z = 10 * 2 // 5 # <--- division and multiplication are equal precedence, so executed in order
print(z)

# Parenthesis will override operator precedence
yy = (10 + 3) * 3 ** 3 # <--- 13 from parenthesis, 3 ** 3 = 27, so 13 * 27 = 351
print(yy)

# Mathematical functions
a = 2.51
print(round(a)) # <--- Rounds to nearest positive integer value
print(abs(a))
print(abs(-1.5)) # <--- Absolute function returns a positive value even on negative numbers

import math # <--- Import a function called math. Call it with a dot[.] operator to see its methods
print(math.ceil(a))
print(math.floor(a))

k = 5
n = 25
print(math.comb(n, k)) # <--- Return number of ways to choose k items from n items without repetition and order

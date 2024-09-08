# using for loops in different scenarios

# loop through each character in a string
number = 0
for letter in "string_of_text":
    number = number + 1
    print(letter , number)


# print 6 times in loop using range, and once outside the loop (non-indented)
for i in range(6):
    print("again")
print("again")


# prints 10, 9, 8 - python is zeio-indexed so counts from 0
num = 10
for i in range(3):
    print(num - i)


# fibonacci challenge - calculate to at least the 20th term based on any two starting values


print("This is the beginning of the fibonacci challenge code")
a = 2
print(a)
b = 5
print(b)
for i in range(18):
    c = a + b
    print(c)
    a = b
    b = c


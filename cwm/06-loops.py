# A for loop can interate over strings, lists and more
for i in "Python":
    print(i)
print("-----------------------------------")

for i in ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]:
    print(i)
print("-----------------------------------")   
    
for i in [1, 2, 3, 4, 5]:
    print(i)
print("-----------------------------------")

for i in range(10):
    print(i)
print("-----------------------------------")

for i in range(25, 30):
    print(i)
print("-----------------------------------")

for i in range(25, 30, 2): # <--- Step to the range function to increase by 2 each time (25, 27, 29)
    print(i)
print("-----------------------------------")


# Calculate the cost of all numbers in a list
basket_cost = 0
for i in [10, 20, 30, 40, 50]:
    basket_cost += i
print(f"The total cost of items in the basket is ${basket_cost}.")
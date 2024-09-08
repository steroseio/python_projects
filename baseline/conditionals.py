# conditionals - different inputs should be able to lead to different outputs

# conditions are checked top to bottom until matched. order overlapping conditions carefully
price = 0
if price == 0:
    print("Bananas are free!")
elif price > 10:
    print("Bananas are more expensive than usual")
elif price < 10:
    print("Bananas are on sale!")
else:
    print("Bananas cost $10")

print("-----------------------------------------")
print("-----------------------------------------")

# conditionals inside loops - the break command quits the loop early 
for price in range(5):
    if price < 5:
        print("I can pay" , price)
    else:
        print("No deal")
        
wallet = 25
for price in range(10):
    #if price < 10:
    if wallet >= price:
        wallet = wallet - price
        print("Now I have" , wallet , "left")
    else:
        print("I can't afford any more")
        break
print("Final amount" , wallet)

print("-----------------------------------------")
print("-----------------------------------------")

# small program using conditionals within a loop
wallet = 20
socks = 0
for price in range(10):
    if wallet >= price:
        wallet = wallet - price
        socks = socks + 1
    else:
        break
if (socks % 2 == 0):
    print("I can pair my socks")
else:
    print("I need one more ...")

print("I have" , wallet , "dollars")
print("and" , socks , "socks")

print("-----------------------------------------")
print("| Collatz Challenge")
print("-----------------------------------------")

number = 27
steps = 0
for i in range(200):
    if number == 1:
        break
    elif number % 2 == 0:
        print("Number is" , number , "this is EVEN, we are at STEP" , steps)
        number = number // 2
        steps = steps + 1
        
    else:
        print("Number is" , number , "this is ODD, we are at STEP" , steps)
        number = number * 3 + 1
        steps = steps + 1
        
if number == 1:
    print("It took" , steps , "steps to get to 1")
else:
    print("The number did not reach 1 yet")
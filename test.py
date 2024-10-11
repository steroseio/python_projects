print("----------------------------------------------")
print("-------   Weight Calculator  -----------------")
print("----------------------------------------------")

weight = input("Weight: ")
measure = input("(K)g or (L)bs: ")

if measure == "K":
    print("Converting to LBS ...")
    sum = int(weight) * 2.2
    print(sum)
else:
    print("Converting to KGS ...")
    sum = int(int(weight) / 2.2)
    print(sum)
    
# convert secs into minutes and return the result

# set variables
seconds = 491
minutes = seconds // 60
#leftover_seconds = seconds - (minutes * 60)
leftover_seconds = seconds % 60

print (seconds , "seconds is the same as")
print (minutes , "minutes and" , leftover_seconds , "seconds")


# extending the program to define full hours as well

# set variables
seconds = 14926
hours = seconds // (60 * 60)
minutes = seconds % (60 * 60) // 60
final_seconds = seconds % 60

print(str(seconds) , "seconds is the same as")
print(str(hours) , "hours," , minutes , "minutes, and" , final_seconds , "seconds.")



# testing python indent
#data = {'a': 0,
#        'b': [[1, 2],
#              [3, 4]],
#        'c':5}
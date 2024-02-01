# Using a range from 1-9 for the * to show the vertical length of the pattern.

star = "*"
for i in range(1,9):
    
# Using <= 4: to show for lines 1-4 the * will go up in increments of 1.
# This is where star = star + "*" is used.
    
    if i <= 4:
        print(star)
        star = star + "*"
        
# Else statement used once line 4 gets to maximum amount of *'s.
# [:-1] being used to show when *'s get to the maximum length which is 5. Starts to go down so each line is less.

    else:
        print(star)
        star = star[:-1]
print("*")
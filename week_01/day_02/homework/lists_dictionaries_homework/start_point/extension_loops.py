# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
a = 0
for a in numbers:
    if a % 2 == 0:    
        print(a)



# 2. Print the difference between the largest and smallest value:

a = min(numbers)
b = max(numbers)

print(int(b)- int(a))


# 3. Print True if the list contains a 2 next to a 2 somewhere.


ace = 0
for ace in numbers:
    if ace == 2 and numbers[numbers.index(ace)+1] == 2:
        print(True)
    


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
zed = [11, 6, 4, 99, 7, 11]
#    would have sum of 22
dont_count = False 
z= 0
total = 0 

for z in zed :
    if z != 6 and dont_count == False:
        total  = total + z 
    elif z == 6: 
        dont_count = True
    elif dont_count == True and z == 7:
        dont_count = False
print(total)
        



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
delta = [5, 13, 2] 
#    would have sum of 5. 

sum = 0
total2 = 0
next_after13 = False

for x in delta:
    if x == 13 :
       next_after13 = True
    elif next_after13 == True:
        next_after13 = False
    else:
        total2 += x
 

print(total2)










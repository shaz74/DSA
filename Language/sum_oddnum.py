# print sum of odd number b/w 1 to 100

sum = 0 
for i in range (1,101):
    if i % 2 != 0:
        sum+=i
        
print(sum)

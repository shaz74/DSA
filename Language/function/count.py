# write a function to count the number of odd and even numbers in an array.

def odd_even_count(arr):
    countOdd = 0
    countEven = 0
    for i in arr:
        if i % 2==0:
            countEven+=1
        else:
            countOdd+=1

    print("even count: ",countEven)
    print("odd count:",countOdd)

odd_even_count([1,2,3,4,5,6,7,8,8,7,9,22,2,5])  


odd_even_count([1,2,2])






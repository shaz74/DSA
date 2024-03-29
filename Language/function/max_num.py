# write a function to find the maximum number in an array

def max_num(arr):
    max = 0
    for i in arr:
        if max < i:
            max = i 

    print(max)
max_num([1,2,3,4,5,6,7])

    

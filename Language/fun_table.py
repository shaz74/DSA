# write a function to print the table of a number 

def multiplication_table(number):
    for i in range(1,11):
        print (f"{number} x {i} = {number * i}")

multiplication_table(5)

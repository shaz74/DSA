# write a function calculator that take 2 number and one operator and calculate.

def calculator(first,second,operator):
    if operator == "+" :
        print("result is :",first + second)
    elif operator == "-":
        print("result is :",first-second)
    elif operator == "*":
        print("result is :",first * second)
    else:
        print("result is ;",first // second)

calculator(1,2,"+")
calculator(2,5,"*")

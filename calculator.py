#"Welcome to my Basic Calculator Version 1"
"""
Only addition, subraction, division,multiplication and Modulus can be performed 
"""
repeat=True
while(repeat):

    while(True):
        num1=(input("Enter first number!    "))
        if  not num1.isnumeric():
            print("pease enter a valid number")
            continue
        break
    while(True):
        oppre=(input("Enter the operator!    "))
        if  oppre not in ["+","-","*","/","%"]:
            print("pease enter a valid operator")
            continue
        break
    while(True):
        num2=(input("Enter second number!   "))
        if  not num2.isnumeric():
            print("please enter a valid number")
            continue
        break
    if (num1 and num2).isnumeric():
        num1,num2=int(num1),int(num2)
        if oppre == "+":
            print("result is",num1+num2)
        elif oppre == "-":
            print("result is",num1-num2)
        elif oppre == "*":
            print("result is",num1*num2)
        elif oppre == "/":
            print("result is",num1/num2)
        elif oppre == "%":
            print("result is",num1%num2)
        else:
            print("please enter a correct operator")
    else:
        print("plase enter a valid number")
    
    if input("press 0 to exit!  ") == "0":
        repeat=False
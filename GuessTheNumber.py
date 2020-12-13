#"Number guessing Roushan"
import os
while(True):
    number = int(input("Enter a number!!\n"))
    os.system("cls")
    while(True):
        choice = int(input("guess the number!  "))
        if str(choice).isnumeric():
            
            if (number > choice):
                print("The actual Number is greater then your Choice made \n",)
                continue
            elif (number < choice):
                print("The actual Number is Lower then your Choice made \n",)
                continue
            elif number == choice:
                print("Conguralation! correct Guess\n",)
                break
            else:
                print("kuch to Gadbad Hai!\n")
        else:
            print("Enter the vakid Number!!!! \n")
            continue
    if input("press 0 to exit!  ") == "0":
        break
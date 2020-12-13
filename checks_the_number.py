import os
while(True):
    actaual_number = int(input("print a number! "))
    higher_number = 10**int(input("number of digit ! "))
    lower_number = 0
    new_number = 0
    iterrations=0

    os.system("cls")

    while(True):

        iterrations+=1

        new_number = int((higher_number+lower_number)/2)
        print("1",new_number,"\t")

        if (actaual_number > new_number ):
            lower_number = new_number
            print("2",lower_number,"\t")
        if (actaual_number < new_number ):
            higher_number = new_number
            print("3",higher_number, "\t")
    
        if (new_number == actaual_number ):
            print("The answer is",int(new_number))
            break

    print("\nnumber of iteration used", iterrations)
    res = input("print 0 to exit")
    if res == 0:
        os.system("cls")
        break


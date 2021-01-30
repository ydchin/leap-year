currYear = input("Enter year: ")
currYear = int(currYear)

if (currYear % 4) == 0:
    if(currYear % 100) == 0:
        if(currYear % 400) == 0:
            print(str(currYear) + " is a leap year")
        else:
            print(str(currYear) + " is not a leap year")
    else:
        print(str(currYear) + " is a leap year")
           
else:
    print(str(currYear) + " is not a leap year")

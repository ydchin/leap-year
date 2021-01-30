while 1:
    currYear = input("Enter year:")
    try:
        currYear = int(currYear)
        break
    except:
        print(currYear + " is not an int! Try again")
        pass

if currYear < 0:
    exit()

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

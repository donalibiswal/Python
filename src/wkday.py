Wkday=int(input("Enter a weekdy number[0-6]:"))

match(Wkday):
    case 0:
        print("Sunday")
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Friday")
    case 5:
        print("Saturday")
    case 6:
        print("Thursaday")
    case _:
        print("Invalid day")
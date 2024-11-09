month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month == 1:
    print("31 days")
elif month == 2:

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 days (Leap year)")
    else:
        print("28 days")
elif month == 3:
    print("31 days")
elif month == 4:
    print("30 days")
elif month == 5:
    print("31 days")
elif month == 6:
    print("30 days")
elif month == 7:
    print("31 days")
elif month == 8:
    print("31 days")
elif month == 9:
    print("30 days")
elif month == 10:
    print("31 days")
elif month == 11:
    print("30 days")
elif month == 12:
    print("31 days")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")

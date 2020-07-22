while True:
    num = input("Please enter a number. ")
    try:
        if (int(num) % 2 > 0):
            print("Your number is odd.")
        if (int(num) % 2 == 0):
            print("Your number is even.")
    except ValueError:
        print("Please enter a number, no letters.")
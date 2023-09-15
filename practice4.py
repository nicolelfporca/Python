while True:
    value = int(input("Enter value: "))

    counter = 0

    while counter <= value:
        if counter % 2 == 0:
            print(f"{counter} Even Number")
        else:
            print(f"{counter} Odd Number")
        counter += 1
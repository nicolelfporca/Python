while True:
    value = int(input("Enter value: "))

    counter = 0
    total = 0

    while counter <= value:
        print(counter)
        total += counter
        counter += 1

    print(f"Total: {total}")
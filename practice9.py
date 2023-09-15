while True:
    number = int(input("Enter number: "))

    i = 1
    factorial = 1

    while i <= number:
        factorial *= i
        i += 1

    print(f"Factorial Number of {number} is {factorial}")
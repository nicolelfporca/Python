while True:
    n = int(input("Enter a number: "))

    def triangle(n):
        if n <= 0:
            return 0
        else:
            return (n * (n + 1)) / 2

    print(triangle(n))
while True:
    def primeNum(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime = int(input("Enter a value: "))

    if primeNum(prime):
        print(f"{prime} is prime number")
    else:
        print(f"{prime} is not prime number")
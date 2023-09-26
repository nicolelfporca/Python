while True:
    def perfectNumber(n):
        if n <= 0:
            return False

        factors = [0]  
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                factors.append(i)
                print(i)

        totalFactors = sum(factors)

        return totalFactors == n

    num = int(input("Enter a number: "))
    print("Factors: ")

    if perfectNumber(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
        
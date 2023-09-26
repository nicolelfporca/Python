while True:
    def SumofDigit(n):
        total = 0
        for i in str(n):
            num = int(i)
            total += num
        return total
    
    number = int(input("Enter a Number: "))

    result = SumofDigit(number)

    print(f"{result}")
    
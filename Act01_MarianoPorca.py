while True: 
    def palindrome(number):
        DigitReverse = str(number)

        return DigitReverse == DigitReverse[::-1]

    num = int(input("Enter a Number: "))

    if palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

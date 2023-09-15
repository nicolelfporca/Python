# def primeNum(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# prime = int(input("Enter a value: "))

# if primeNum(prime):
#     print("Prime number")
# else:
#     print("Not a prime number")

def primeNum(n):
    counter = 2
    count = 0
    while counter <= n:
        if n % counter == 0:
            count += 1
        counter += 1
    return count

prime = int(input("Enter a value: "))

if primeNum(prime+1) > 1:
    print("Not a prime number")
else:
    print("Prime number")

# Output
# Enter a value: 2
# Prime number
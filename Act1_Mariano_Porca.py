n1 = int(input("input n1: "))
n2 = int(input("input n2: "))
x = n1

product = 0
quotient = 0
remainder = 0

for i in range(1, n2+1):
    product += n1

while n1 >= n2:
    n1 -= n2
    quotient += n1

for i in range(n1):
    remainder += n1
    if remainder < n2:
        break

print(f"product of {x} and {n2} is: {product}")
print(f"quotient of {x} and {n2} is: {quotient}")
print(f"remainder of {x} and {n2} is: {remainder}")

# Sir Efren’s Codes

# num1 = int(input("Input value for num1: "))
# num2 = int(input("Input value for num2: "))
# product = 0
# counter = 0
# num_1 = 0
# for i in range(1, num2+1):
#     product += num1
# print(f"Total product of {num1} and {num2} is : {product}")

# if (num2 > num1):
#     print(f"Total integer quotient of {num1} and {num2} is : 0")
#     print(f"Total integer remainder of {num1} and {num2} is : {num1}")

# else:
#     num_1 = num1
#     while num1 > num2:
#         num1 -= num2
#         counter += 1
#     print(f"Total integer quotient of {num_1} and {num2} is : {counter}")
#     print(f"Total integer remainder of {num_1} and {num2} is : {num1}")
n = int(input("input number: "))

while n != 1:
    print(n)

    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

print(n)

# Sir Efren’s Codes

# num = int(input("Input integer value: "))
# odd = 0

# while num != 1:
#     if num % 2 == 0:
#         num = num / 2
#         print(int(num))
#     else:
#         num = num * 3 + 1
#         print(int(num))
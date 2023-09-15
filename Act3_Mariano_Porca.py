# No Answer

# Sir Efren’s Codes

cc = str(input("Credit Card number: "))
cn = len(cc) - 1
# start index length - 1
# Let's say we have 16 digits so length is 15 by using length - 1

product = 0
other = 0
x = 0

while cn >= 0:
    if cn % 2 == 1:
        other += int(cc[cn])
    else:
        product = int(cc[cn]) * 2
        if product > 9:
            x += (int(product) % 10) + int(product/10)
        else:
            x += product
    cn -= 1

if int(other + x) % 10 == 0:
    print(f"{cc} is valid number")
else:
    print(f"{cc} is invalid number")
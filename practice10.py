while True:
    base = int(input("Enter number: "))
    num = ((base - 1) * base + 1)

    total = 0
    counter = 1

    while counter <= base:
        total += num
        print(num)
        num += 2
        counter += 1
   
    print(f"Total: {total}")
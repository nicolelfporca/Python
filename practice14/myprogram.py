import myfunctions as mf

while True:
    first = int(input("input first value: "))
    second = int(input("input second value: "))


    sum = mf.addition(first,second)
    difference = mf.subtraction(first,second)


    print(f"sum is {sum}")
    print(f"difference is {difference}")
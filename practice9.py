while True:
    def operation(oper,n1,n2):
        if oper == "+":
            print(f"{n1 + n2}")
        elif oper == "-":
            print(f"{n1 - n2}")
        elif oper == "*":
            print(f"{n1 * n2}")
        elif oper == "/":
            print(f"{n1 / n2}")  
        elif oper == "%":
            print(f"{n1 % n2}")    
        else:
            print("Invalid input")

    str = input("Input arithmetic operation: ")
    operation(str,100,200)

# Output
# Input arithmetic operation: +
# 300
# Input arithmetic operation: -
# -100
# Input arithmetic operation: *
# 20000
# Input arithmetic operation: /
# 0.5
# Input arithmetic operation: %
# 100

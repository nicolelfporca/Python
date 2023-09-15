def oddEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
   
for i in range(1,30):
    # if(oddEven(i)):
    #     print(f"{i} - even")
    # else:
    #     print(f"{i} - odd")
    if(oddEven(i)) == False:
        print(f"{i} - odd")

# Output
# 1 - odd
# 3 - odd
# 5 - odd
# 7 - odd
# 9 - odd
# 11 - odd
# 13 - odd
# 15 - odd
# 17 - odd
# 19 - odd
# 21 - odd
# 23 - odd
# 25 - odd
# 27 - odd
# 29 - odd
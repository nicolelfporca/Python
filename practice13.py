def factorial(n):
    i = 1
    while n > 1:
        i *= n
        n -= 1
    return i

print(factorial(5))

# Output
# 120
input = input("Enter your name and favorite number: ")

digits = 0
letters = 0

for count in input:
    if count.isdigit():
        digits += 1
    elif count.isalpha():
        letters += 1
    else:
        pass

print("LETTERS: ", letters)
print("DIGITS: ", digits)
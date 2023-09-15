list = []

while True:
    value = input("Enter a value: ")
    list.append(value)
   
    value2 = input("Do you want to enter another value? (Y/N): ")
    if value2 != 'y':
        break

print("Total number of words:", len(list))
for value in list:
    print(value)
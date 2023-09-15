record = {}


while True:
    print("\nRecord Keeping App")
    print('a. Add Data', '\nb. Delete Data', '\nc. End\n')

    choices = input("Enter your choice: ")

    if choices == 'a':
        print("=====ADD NEW RECORD=====")
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        record[key] = value

        print("=====DISPLAY RECORD=====")
        for key, value in record.items():
            print(f"{key} : {value}")
        print("=====END OF RECORD=====")

    elif choices == 'b':
        print("=====DELETE RECORD=====")
        key = input("Enter Key: ")
        if key in record:
            record.pop(key)
        print("=====DISPLAY RECORD=====")
        for key, value in record.items():
            print(f"{key} : {value}")
        print("=====END OF RECORD=====")

    elif choices == 'c':
        print("Thank you!")

    else:
        print("Choices not found")
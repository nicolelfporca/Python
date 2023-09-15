while True:
    grade = float(input("Enter grade: "))

    if grade >= 99 and grade <= 100:
        print("Excellent")
    elif grade >= 95 and grade <= 99:
        print("Very Good")
    elif grade >= 90 and grade <= 94:
        print("Good")
    elif grade >= 85 and grade <= 89:
        print("Satisfactory")
    elif grade >= 80 and grade <= 84:
        print("Fair")
    elif grade >= 75 and grade <= 79:
        print("Poor")
    elif grade >= 50 and grade <= 74:
        print("Failed")
    else:
        print("Grade Invalid")
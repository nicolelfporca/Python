elective = "Python"

def showName():
    global elective
    print(f"Function 1: {elective}")
    elective = "Visual C#"
    print(f"Function 2: {elective}")

print(f"Main program 1: {elective}")
showName()
print(f"Main program 2: {elective}")

# Output
# Main program 1: Python
# Function 1: Python
# Function 2: Visual C#
# Main program 2: Visual C#

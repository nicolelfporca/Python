score_counts = {}

while True:
    user_input = input("Enter a test score: ")
    if user_input == "0":
        break
    try:
        score = int(user_input)
        if score >= 0:
            if score in score_counts:
                score_counts[score] += 1
            else:
                score_counts[score] = 1
        else:
            print("Enter a positive integer.")
    except ValueError:
        print("Invalid input.")

sorted_scores = sorted(score_counts.items())

print(f"Test Score \t Count")
for score, count in sorted_scores:
    print(f"{score} \t\t {count}")

# Jasper’s Codes

# while True:
#     numbers = str(input("Sample data set: "))
#     list = numbers.split(" ")

#     for i in range(0, len(list)):
#         list[i] = int(list[i])

#     list.sort()
#     convertedSet = sorted(set(list))

#     print("Test Score \tCount")
   
#     for test_scores in convertedSet:
#         print(str(test_scores) + "\t\t" + str(list.count(test_scores)))
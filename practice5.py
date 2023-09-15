total = 0

for i in range(1,20):
    total += i
   
    if total >= 75:
        print("Reached 75")
        # break

print(f"Total Value: {total}")
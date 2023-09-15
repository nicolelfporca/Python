total = 0

for i in range(1,20):
    total += i
   
    if i % 2 == 1:
        total += i
        continue

print(f"Total Value: {total}")
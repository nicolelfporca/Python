total = 0
i = 0

while i <=5:
    i += 1
    if i % 2 == 1:
        continue
    total += i

print(f"Total Value: {total}")
S = 0

for x in range(1,11):
    if (x%2 == 0):
        S = S - (1/x)
    else:
        S = S + (1/x)
print(f"S = {S:.2f}")
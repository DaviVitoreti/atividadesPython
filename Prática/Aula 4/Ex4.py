F = 30
C = 0

for const in range(30, 51):
    C = (F - 32) * (5/9)
    print(f"{F}°F = {C:.2f}°C")
    F += 1
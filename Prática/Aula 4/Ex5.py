S = 0
var1 = 1
var2 = 1

for var2 in range(1, 51):
    S = S + (var1 / var2)
    var1 += 2
    var2 += 1
else:
    print(f"{S:.2f}")
result = []
for i in range(9):
    result.append(int(input()))

m = max(result)
n = result.index(max(result))
print(m)
print(n+1)
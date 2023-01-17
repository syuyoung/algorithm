N = int(input())
result = []
for i in range(N):
    result.append(int(input()))
result.sort()

for num in result:
    print(num)
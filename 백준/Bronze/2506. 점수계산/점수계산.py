N=int(input())
numbers = list(map(int,input().split()))
point = 0
result = 0
for i in range(N):
    if numbers[i] == 1:
        point += 1
        result += point
    else:
        point = 0
print(result)
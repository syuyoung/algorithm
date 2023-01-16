N, X = list(map(int,input().split()))
numbers = list(map(int,input().split()))
list = []
for i in numbers:
    if i < X:
        list.append(i)
print(*list)
N = int(input())
numbers = map(int, input().split())
list = []
cnt = 0
for i in numbers:
    if i not in list:
        list.append(i)
    elif i in list:
        cnt += 1
print(cnt)
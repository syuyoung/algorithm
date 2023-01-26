n = int(input())
numbers = list(map(int,input().split()))
num = int(input())
cnt = 0
for i in numbers:
    if i == num:
       cnt +=1
print(cnt) 
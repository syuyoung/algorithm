import sys
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
    
r_li = reversed(li)

cnt = 0
max = 0

for i in r_li:
    if max < i:
        max = i
        cnt += 1
print(cnt)
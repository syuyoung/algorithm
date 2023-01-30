import sys
input = sys.stdin.readline
result = 0
num = 0
for i in range(5):
    N = sum(map(int,input().split()))
    if N > result:
        result = N
        num = i+1
print(num,result)
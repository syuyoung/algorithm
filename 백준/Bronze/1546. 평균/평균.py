import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
result = []
n = 0
mx = max(num)
for i in num:
    n = i/mx*100
    result.append(n)
print(sum(result)/N)
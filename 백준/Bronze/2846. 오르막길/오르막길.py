import sys
input = sys.stdin.readline

n = int(input())
way = list(map(int, input().split()))
num = 0
result = []
#1 2 1 4 6
for i in range(n-1):
    if way[i] < way[i+1]:
        num += way[i+1] - way[i]

    elif way[i] >= way[i+1]:
        result.append(num)
        num = 0
    
result.append(num)
print(max(result))
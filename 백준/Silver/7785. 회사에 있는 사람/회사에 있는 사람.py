import sys
input = sys.stdin.readline

N = int(input())
office = {}
for i in range(N):
    a, b = input().split()
    if b == 'enter':
        office[a] = 'enter'
    elif office[a]:
        del office[a]

result = sorted(office.keys(), reverse=True)
for i in result :
    print(i)
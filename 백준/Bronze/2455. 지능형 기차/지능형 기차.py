import sys

people = []
result = 0

for _ in range(4):
    a, b = map(int,sys.stdin.readline().split())
    result += b
    result -= a

    people.append(result)

print(max(people))
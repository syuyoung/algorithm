T = int(input())

for t in range(1, T + 1):
    a, b = list(map(int,input().split()))
    x = a // b
    y = a % b
    print(f"#{t} {x} {y}")
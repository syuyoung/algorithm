T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int,input().split()))
    num = sum(numbers)
    print(f"#{t} {round(num / len(numbers))}")
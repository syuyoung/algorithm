T = int(input())

for i in range(1, T+1):
    N = int(input())
    coin = [25, 10, 5, 1]
    result = []
    for i in coin:
        result.append(N//i)
        N %= i
    print(*result)
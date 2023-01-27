import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    numbers = list(map(int,input().split()))
    avg = sum(numbers[1:]) / numbers[0]
    cnt = 0
    for i in numbers[1:] :
        if i > avg :
            cnt += 1
    print(f'{cnt/numbers[0] *100:.3f}%')
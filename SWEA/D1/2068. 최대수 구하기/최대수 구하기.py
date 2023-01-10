T = int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    num = [x for x in numbers if 0 <= x <= 10000]
    a = max(num)
    
    print(f'#{t} {a}')
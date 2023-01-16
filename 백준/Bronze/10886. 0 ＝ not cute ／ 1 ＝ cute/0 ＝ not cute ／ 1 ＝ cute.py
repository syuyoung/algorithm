T = int(input())
result = 0
for t in range(1, T+1):
    N = int(input())

    for i in range(N):
        result += N
if result > T//2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
T = int(input())

for _ in range(1, T+1):
    ox_list = list(input())
    cnt = 0
    result = 0
    for ox in ox_list:
        if ox == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)

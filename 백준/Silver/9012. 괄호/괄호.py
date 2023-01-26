T = int(input())
for i in range(1, T+1):
    word = list(input())
    cnt = 0

    for i in word:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt == 0:
        print('YES')
    elif cnt >0:
        print('NO')
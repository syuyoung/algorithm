import sys

input = sys.stdin.readline

T = int(input())
for _ in range(1, T+1):
        score = list(map(int, input().split()))
        score = sorted(score)
        if score[-2]-score[1] >= 4:
            print('KIN')
        else:
            print(sum(score[1:4]))
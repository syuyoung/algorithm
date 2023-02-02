import sys

input = sys.stdin.readline

w = [int(input()) for _ in range(10)]
w = sorted(w)
k = [int(input()) for _ in range(10)]
k = sorted(k)
print(sum(w[-3:]), sum(k[-3:]))
import sys

a,b = sys.stdin.readline().split()

a = list(map(int,a))
b = list(map(int,b))
print(sum(a)*sum(b))
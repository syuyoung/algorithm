import sys

list = [int(input()) for _ in range(3)]
result = str(list[0]*list[1]*list[2])
for i in range(10):
    print(result.count(str(i)))
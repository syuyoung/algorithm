import sys

input = sys.stdin.readline
from collections import deque

queue = deque([])
for _ in range(int(input())):
    word = input().split()
    if word[0] == 'push':
        queue.append(word[1])
    elif word[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif word[0] == 'size':
        print(len(queue))
    elif word[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif word[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
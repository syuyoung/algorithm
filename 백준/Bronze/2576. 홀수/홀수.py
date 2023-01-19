import sys

n = 7
list = [int(input()) for _ in range(n)]
odd = []
even = []

for i in list:
    if (i) % 2 ==1:
        odd.append(i)
    elif (i) % 2 == 0:
        even.append(i)
if len(odd) != 0:
    print(sum(odd))
    print(min(odd))
else:
    print('-1')
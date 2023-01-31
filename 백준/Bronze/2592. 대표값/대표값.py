import sys

N_list = [int(sys.stdin.readline()) for _ in range(10)]

print(sum(N_list)//10)
print(max(N_list, key = N_list.count))
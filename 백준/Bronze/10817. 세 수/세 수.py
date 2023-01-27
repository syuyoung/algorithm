import sys

input = sys.stdin.readline

numbers = list(map(int,input().split()))
numbers = sorted(numbers)
print(numbers[1])
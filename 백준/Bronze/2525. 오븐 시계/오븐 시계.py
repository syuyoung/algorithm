import sys

input = sys.stdin.readline

a,b = map(int,input().split())
c = int(input())

hours = int((a*60+b+c)/60)
minutes = int((a*60+b+c)%60)
if(hours>23):
    hours = hours-24
print(hours, minutes)
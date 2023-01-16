a, b, c = list(map(int,input().split()))
list = []
if a == b == c:
    list = 10000+a*1000
elif a == b:
    list = 1000+a*100
elif b == c:
    list = 1000+b*100
elif a == c:
    list = 1000+c*100
else:
    list = [a,b,c]
    list = sorted(list)
    list = list[2]*100

print(list)
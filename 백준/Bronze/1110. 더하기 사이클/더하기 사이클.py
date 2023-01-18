n = input()
i = n
if int(i) < 10:
    i= '0' + i
cnt = 0
while True:

    first = i[-1]
    second = i[0]
    sum_number = int(first) + int(second)
    new_number = i[-1] + str(sum_number)[-1]
    cnt += 1
    if int(new_number) == int(n):
        break
    i = new_number

print(cnt)
name1 = int(input())
name2 = int(input())
name3 = int(input())
name4 = int(input())
name5 = int(input())
list = [name1, name2, name3, name4, name5]
fix_list = []
for i in list:
    if i < 40:
        fix_list.append(40)
    else :
        fix_list.append(i)
avg = sum(fix_list) / len(fix_list)
print(round(avg))
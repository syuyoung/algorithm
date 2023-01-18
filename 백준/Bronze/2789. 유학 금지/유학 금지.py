word = list(input())
block = ['C','A','M','B','R','I','D','G','E']
result = []
for i in word:
    if i not in block:
        result.append(i)
print(''.join(result))
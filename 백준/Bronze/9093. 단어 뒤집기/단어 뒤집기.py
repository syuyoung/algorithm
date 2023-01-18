T = int(input())

for t in range(1, T+1):
    string = input() # 문장 입력
    reverse = string[::-1].split()# 문장 거꾸로 출력 후 리스트로 변환
    result = reverse[::-1]#리스트 거꾸로 출력
    print(*result)
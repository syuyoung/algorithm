string = input()
string_len = len(string) #길이 지정
for i in range(0, string_len , 10): # 0부터 string  길이까지 반복하는데 10개씩
    print(string[i:i + 10]) #0~10 10개씩 출력
input_numbers=list(map(int,input().split()))

numbers = []

for number in input_numbers:
    numbers.append(int(number))
while True:
    for i in range(0, len(numbers) -1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            print(*numbers)
    if numbers == [1, 2, 3, 4, 5]:
        break
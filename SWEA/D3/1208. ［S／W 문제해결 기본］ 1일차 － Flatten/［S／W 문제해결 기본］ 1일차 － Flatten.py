T = 10
for t in range(1, T+1):
    N = int(input())
    box = list(map(int,input().split()))
    for i in range(N):
        max_box = max(box)
        min_box = min(box)
        max_idx = box.index(max_box)
        min_idx = box.index(min_box)
        box[max_idx] -= 1
        box[min_idx] += 1
    print(f'#{t} {max(box) - min(box)}')
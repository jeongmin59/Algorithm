# 1208_Flatten

for tc in range(1, 11):  # T = 10
    dump = int(input())  # 제한된 횟수
    box_h = list(map(int, input().split()))

    for _ in range(dump):

        max_b = max(box_h)
        min_b = min(box_h)

        idx_max_b = box_h.index(max_b)
        idx_min_b = box_h.index(min_b)

        box_h[idx_max_b] = box_h[idx_max_b] - 1  # 최대값의 인덱스에 -1
        box_h[idx_min_b] = box_h[idx_min_b] + 1

        new_max = max(box_h)
        new_min = min(box_h)

        if new_max - new_min < 2:
            break

    print(f'#{tc} {new_max - new_min}')

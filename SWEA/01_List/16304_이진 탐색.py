# 16304_이진 탐색

def binarySearch(page, key):
    left = 1  # 시작
    right = page  # 마지막
    cnt = 0  # 찾고자 하는 값을 찾으면 몇 번 이진탐색 했는지 카운팅

    while left <= right:
        cnt += 1
        c = (left + right) // 2  # 중간 페이지 계산

        if c == key:  # 찾는 쪽 번호가 같아질 경우
            return cnt
        elif c < key:  # 중간 페이지가 목표보다 작으면
            left = c  # 시작 페이지를 중간 페이지부터
        else:
            right = c  # 끝 페이지를 중간 페이지로
    return False  # 못 찾을 경우 반환


T = int(input())
for tc in range(1, T + 1):
    page, pa, pb = map(int, input().split())

    p1 = binarySearch(page, pa)
    p2 = binarySearch(page, pb)

    if p1 == p2:
        print(f"#{tc} 0")
    elif p1 > p2:
        print(f"#{tc} B")
    else:
        print(f"#{tc} A")

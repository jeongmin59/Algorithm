# 16340_문자열 비교

T = int(input())

for tc in range(1, T + 1):
    s = str(input())
    ss = str(input())

    if s in ss:
        print(f"#{tc} 1")

    else:
        print(f"#{tc} 0")

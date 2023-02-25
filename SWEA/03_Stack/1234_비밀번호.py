# 1234_비밀번호

for tc in range(1, 11):
    n, pw = input().split()
    n = int(n)
    pw = list(pw)

    s = 0

    while s < len(pw):      # 이전 값과 비교해 없애고, 하나 전 인덱스로 이동해 확인
        if s and pw[s] == pw[s-1]:  # s가 0이 아닐 때 이전 값과 비교
            del pw[s], pw[s-1]
            s -= 1
        else:
            s += 1

    print(f"#{tc} {''.join(pw)}")

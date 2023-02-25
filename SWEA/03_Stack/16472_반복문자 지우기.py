# 16472_반복문자 지우기

T = int(input())

for tc in range(1, T + 1):
    s = list(input())

    cnt = 0
    while cnt < len(s):
        for i in range(1, len(s)):
            # print(s[i-1], s[i])

            if s[i - 1] == s[i]:
                del s[i]
                del s[i - 1]
                break  # 한 번하고 끝내줌 - 길이 변화 때문
        cnt += 1

    print(f"#{tc} {len(s)}")

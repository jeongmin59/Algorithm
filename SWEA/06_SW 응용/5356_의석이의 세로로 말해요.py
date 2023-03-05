# 5356_의석이의 세로로 말해요
'''
- 주어진 배열을 세로로 읽고 이어 붙여서 출력
- 개수가 다를 때 어떻게 이어 붙일지가 관건

- 최대 길이에 맞춰서 이어 붙이면 됨
or
- 모자란 길이에 공백이든 뭐든 채워서 그것을 제외하고 이어붙여도 됨
'''

T = int(input())
for tc in range(1, T + 1):
    text = [list(input()) for _ in range(5)]

    txt = [[0 for _ in range(15)] for _ in range(15)]

    for i in range(len(text)):
        for j in range(len(text[i])):
            txt[i][j] = text[i][j]

    ans = ""
    for k in range(15):
        for l in range(15):
            if txt[l][k] != 0:
                ans += txt[l][k]

    print(f"#{tc} {ans}")

    # max_t = 0
    # for t in text:
    #     if len(t) > max_t:
    #         max_t = len(t)
    #
    # txt = ""
    # for i in range(max_t):
    #     for j in range(5):
    #         if i < len(text[j]):
    #             txt += text[j][i]
    #
    # print(f"#{tc} {txt}")

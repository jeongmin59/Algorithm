# 1961_숫자 배열 회전

# i는 행, j는 열

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    # 2차원 행렬 초기화
    lst_90 = [[0 for _ in range(n)] for _ in range(n)]
    lst_180 = [[0 for _ in range(n)] for _ in range(n)]
    lst_270 = [[0 for _ in range(n)] for _ in range(n)]

    # 90도로 회전 했을 때
    for i in range(n):
        for j in range(n):
            lst_90[i][j] = lst[n - j - 1][i]

    # print(lst_90)

    # 180도로 회전 했을 때
    for i in range(n):
        for j in range(n):
            lst_180[i][j] = lst_90[n - j - 1][i]

    # 270도로 회전 했을 때
    for i in range(n):
        for j in range(n):
            lst_270[i][j] = lst_180[n - j - 1][i]

    # 공백 없이 출력 하려면...
    print(f'#{tc}')
    for i in range(n):
        print("".join(map(str, lst_90[i])), end=" ")      # lst[i]를 뽑으면 각 행이 출력됨 (리스트 벗겨진 채로)
        print("".join(map(str, lst_180[i])), end=" ")
        print("".join(map(str, lst_270[i])), end=" ")
        print()     # enter

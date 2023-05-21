# 1961_숫자 배열 회전

def change_90(lst, N):
    new_lst = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_lst[i][j] = lst[N - 1 - j][i]
    return new_lst


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [input().split() for _ in range(N)]

    lst_90 = change_90(lst, N)
    lst_180 = change_90(lst_90, N)
    lst_270 = change_90(lst_180, N)

    print(f"#{tc}")
    for a, b, c in zip(lst_90, lst_180, lst_270):
        a1 = ''.join(a)
        b1 = ''.join(b)
        c1 = ''.join(c)
        print(a1, b1, c1)

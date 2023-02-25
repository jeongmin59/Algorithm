# 2005_파스칼의 삼각형

# 첫 번째 줄은 항상 숫자 1 고정
# 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성됨
# n * n

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    pascal = [[0] * (n + 1) for _ in range(n + 1)]

    pascal[1][1] = 1    # 초기값
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    print(f"#{tc}")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(pascal[i][j], end=" ")
        print()

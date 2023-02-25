# 16495_종이 붙이기(DP)

# 배열 n이 주어졌을 때 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 하는지
# 주어진 종이: 10 * 20, 20 * 20
# n은 10의 배수

def paper(n):
    n //= 10  # n = n // 10
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 3

    for i in range(3, n + 1):
        f[i] = f[i - 2] * 2 + f[i - 1]  # 규칙

    return f[n]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    print(f"#{tc} {paper(n)}")

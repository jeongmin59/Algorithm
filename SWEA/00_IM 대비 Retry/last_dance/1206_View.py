# 1206_View
'''
- 좌, 우로 2칸씩 조망권 확보 되어야 함
* 풀이
- [i-2], [i-1], [i+1], [i+2] 값들 중 가장 큰 값이랑 [i]를 비교...
- 좌, 우 0씩 2칸 있으니 i의 범위만 잘 정하면 됨
'''
for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    maxV = 0
    for i in range(2, N-2):
        maxV = max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
        if maxV < lst[i]:
            ans += (lst[i] - maxV)

    print(f"#{tc} {ans}")

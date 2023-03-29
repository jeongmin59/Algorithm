# 3985_롤 케이크
'''
- P번 부터 K번까지 받고 싶어함
- 가장 많이 받을 것으로 예상 되는 사람, 가장 많이 받은 사람 출력...
'''

L = int(input())
N = int(input())
cake = [1] * (L + 1)    # 케이크를 직접 가져 감
mx1 = mx2 = mx1_i = mx2_i = 0   # mx1은 가장 많이 원한 사람, mx2는 가장 많이 가져간 사람

for i in range(1, N + 1):   # 고객 번호는 1번이니까 1부터 = 방청객 번호 순
    p, k = map(int, input().split())
    if mx1 < (k - p + 1):   # 원하는 개수가 가장 큰 값이면 갱신
        mx1 = k - p + 1
        mx1_i = i   # 방청객 번호

    cnt = sum(cake[p: k + 1])   # 실제 i번 방청객이 받은 개수
    if mx2 < cnt:
        mx2 = cnt
        mx2_i = i
    cake[p: k + 1] = [0] * (k - p + 1)  # 가져간 만큼 개수를 0으로 처리

print(mx1_i)
print(mx2_i)

# 2999_비밀 이메일
'''
- R <= C이고 R * C = N
- R == 행, C == 열
'''

message = input()
M = len(message)

lst = []    # M의 약수들만 담길 리스트
for i in range(1, M + 1):   # 1부터 M까지 M이 i에 나누어 떨어지면
    if M % i == 0:
        lst.append(i)

R = C = 0
if len(lst) % 2 == 0:   # 약수 짝수 개면
    R = lst[len(lst) // 2 - 1]  # 왼쪽 중 큰 약수
    C = lst[len(lst) // 2]  # 오른쪽 중 가장 작은 약수
else:
    R = C = lst[len(lst) // 2]  # 약수 홀수 개면

email = [[''] * C for _ in range(R)]
for c in range(C):
    for r in range(R):
        email[r][c] = message[c * R + r]

ans = ''
for r in range(R):
    for c in range(C):
        ans += email[r][c]

print(ans)

# 13300_방 배정
'''
- 한 방에는 같은 성별끼리, 같은 학년끼리 배정, 한 명만 배정하는 것도 가능
- 조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램 작성
- N: 학생 수, K: 최대 인원 수, S: 성별, Y: 학년

1. 빈 2차원 배열 만들기 (성별 2개, 학년 6개)
2. 입력 받을 때 학생 수 카운트
3. 최대 인원수에 맞게 떨어지면 ans에 더하고, 그렇지 않으면 +1 한 것을 더함
'''

N, K = map(int, input().split())
students = [[0 for _ in range(6)] for _ in range(2)]

for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y - 1] += 1     # 학생 수 카운트

ans = 0
for i in range(2):  # 성별
    for j in range(6):  # 학년
        if students[i][j] % K == 0:     # 최대 인원수 맞게 떨어질 때
            ans += students[i][j] // K
        else:
            ans += students[i][j] // K + 1

print(ans)

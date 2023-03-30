# 8958_OX퀴즈

'''
- X를 만났을 때 숫자를 세던 변수 초기화 해주면 됨
- ATM 문제와 유사
'''

N = int(input())
for _ in range(N):
    quiz = input()

    cnt = ans = 0
    for i in quiz:
        if i == 'O':
            cnt += 1
            ans += cnt
        elif i == 'X':
            cnt = 0

    print(ans)

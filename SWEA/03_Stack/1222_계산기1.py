# 1222_계산기1

T = 10

for tc in range(1, T + 1):
    n = int(input())
    s = input()  # 문자열로 받음

    stack = []
    postfix = ""  # 후위표기식 문자열
    cal = []  # 계산할 스택

    # 후위표기식으로 변환하기
    for i in s:
        if not stack and i == "+":  # 스택 비었으면 연산자 넣기
            stack.append(i)

        elif stack and i == "+":  # 이미 +가 있으면 빼고 넣기
            postfix += stack.pop()
            stack.append(i)

        else:  # 숫자면 그냥 추가
            postfix += i

    else:  # 남아있는 마지막 + 제거
        postfix += stack.pop()

    # 결과 값 계산
    for i in postfix:
        if i != "+":  # 숫자면 cal 스택에 넣기
            cal.append(int(i))

        elif i == "+":  # 연산자이면 스택의 숫자 2개 꺼내서 더하고 넣기
            num2 = cal.pop()
            num1 = cal.pop()
            cal.append(num1 + num2)

    print("#{} {}".format(tc, *cal))

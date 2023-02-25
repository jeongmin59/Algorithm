# 1223_계산기2

for tc in range(1, 11):
    n = int(input())    # tc 길이
    s_lst = input()

    stack = []
    postfix = ""
    cal = []    # 계산할 스택

    # 후위표기식으로 변환
    for s in s_lst:
        if not stack:       # 빈 스택일 때
            if s == "+" or s == "*":
                stack.append(s)
                continue
        # 빈 스택 아닐 때
        if s == "+":
            if stack[-1] == "+":
                postfix += stack.pop()
                stack.append(s)
            elif stack[-1] == "*":
                while stack:
                    postfix += stack.pop()
                stack.append(s)
        elif s == "*":
            if stack[-1] == "+":
                stack.append(s)
            elif stack[-1] == "*":
                postfix += stack.pop()
                stack.append(s)
        else:   # 숫자일 때
            postfix += s
    else:       # 마지막 남은 거 제거
        postfix += stack.pop()

    # 계산하기...
    for p in postfix:
        if p != "+" and p != "*":
            cal.append(int(p))
        elif p == "+":
            num2 = cal.pop()
            num1 = cal.pop()
            cal.append(num1 + num2)
        elif p == "*":
            num2 = cal.pop()
            num1 = cal.pop()
            cal.append(num1 * num2)

    print(f"#{tc} {sum(cal)}")

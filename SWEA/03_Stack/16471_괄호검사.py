# 16471_괄호검사

T = int(input())

for tc in range(1, T + 1):
    line = input()

    stack = []
    answer = 1

    for i in line:
        if i == "(" or i == "{":
            stack.append(i)
        # 닫힌 괄호가 온다면
        elif i == ")" or i == "}":
            if not stack:  # 빈 스택에 들어오면 안 됨
                answer = 0
            # pop 실행시키면서 맞는지 확인
            elif i == ")" and stack.pop() != "(":  # 안 맞다는 거임
                answer = 0
            elif i == "}" and stack.pop() != "{":  # 얘도
                answer = 0
    if stack:  # 스택에 괄호가 남아있다면
        answer = 0

    print(f"#{tc} {answer}")

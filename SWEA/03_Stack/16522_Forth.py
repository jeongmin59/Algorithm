# 16522_Forth

T = int(input())

for tc in range(1, T + 1):
    forth = list(input().split())

    stack = []
    ans = 1  # true

    for i in range(len(forth) - 1):  # 마지막은 .이니까
        if forth[i].isdigit():  # 숫자면 스택에 push
            stack.append(forth[i])

        else:
            try:
                # 연산할 숫자 2개 뽑기
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if forth[i] == "+":
                    stack.append(num1 + num2)
                elif forth[i] == "-":
                    stack.append(num1 - num2)
                elif forth[i] == "*":
                    stack.append(num1 * num2)
                elif forth[i] == "/":
                    stack.append(num1 // num2)  # 나머지 필요 x

            except:  # 예외인 것만 false 처리
                ans = False
    if ans == False or len(stack) != 1:
        print(f"#{tc} error")
    else:
        print(f"#{tc} {stack.pop()}")

# 1225_암호생성기

# 8개의 숫자를 받은 후, 첫 번째 숫자를 -1한 뒤, 맨 뒤로 보냄
# 두 번째는 -2, 그 다음은 -3 ... -5까지 하는 작업을 한 사이클이라고 함
# 숫자가 감소할 때 0보다 작거나 같으면 0으로 출력 후 break

for tc in range(1, 11):  # 테스트 케이스 개수: 10개
    t = int(input())
    pw = list(map(int, input().split()))

    cnt = 1  # 감소할 값
    while True:
        q = pw.pop(0) - cnt  # pop한 값에 -cnt로 숫자 감소

        if q <= 0:  # 꺼내는 값이 0보다 작거나 같으면
            pw.append(0)
            break

        else:
            pw.append(q)
            cnt += 1

        if cnt > 5:  # -1~-5가 한 사이클
            cnt = 1  # 초기화

    print(f"#{tc}", *pw)

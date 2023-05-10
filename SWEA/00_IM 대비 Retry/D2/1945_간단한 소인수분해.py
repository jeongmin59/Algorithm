# 1945_간단한 소인수분해
'''
- 2, 3, 5, 7, 11의 지수는 a, b, c, d, e 이다.
- 지수를 구해서 출력
* 풀이
- 2, 3, 5, 7, 11 배열과 빈 배열을 만든다.
- 입력 받은 값을 나눌 수 있을 만큼 나누고, 나눈 횟수를 cnts += 1
- 나누었던 값을 갱신 하면서 반복문을 실행한다.
'''
T = int(input())
divs = [2, 3, 5, 7, 11]     # 소인수로 사용될 리스트

for tc in range(1, T + 1):
    num = int(input())
    cnts = [0] * 5

    for i in range(5):
        while num % divs[i] == 0:   # 소인수로 나누어질 수 있는 만큼 나누기
            cnts[i] += 1            # 나눈 횟수를 cnts에 저장
            num //= divs[i]         # 해당 소인수로 갱신

    print(f"#{tc}", *cnts)

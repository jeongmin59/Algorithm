# 10431_줄 세우기
'''
- 키가 가장 작은 학생이 1번... 가장 큰 학생이 20번임
- 항상 20명이고, 같은 키를 가진 학생은 한 명도 없음
- 자신 보다 키가 큰 학생이 있을 경우, 가장 앞에 있는 학생 앞에 선다
- 이 때 모든 학생들은 한 발씩 뒤로 물러 서게 된다.
- 오름차순으로 정렬 되었을 때 학생들이 총 몇 번 뒤로 물러 서게 되는지 걸음 수의 총합 출력
'''

P = int(input())
for tc in range(1, P+1):
    height = list(map(int, input().split()))[1:]

    cnt = 0
    for i in range(1, 20):
        for j in range(0, i):
            if height[i] < height[j]:
                cnt += 1

    print(f"{tc} {cnt}")


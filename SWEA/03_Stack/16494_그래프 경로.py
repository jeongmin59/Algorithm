# 16494_그래프 경로

# V개 이내 노드 , E개의 간선, 경로가 있으면 1, 없으면 0

def dfs(start, goal):
    stack.append(start)
    visited[start] = 1
    while stack:
        if start == goal:
            return 1
        else:
            for i in node[start]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = 1
            start = stack.pop()
    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    node = [[] for _ in range(V + 1)]

    stack = []
    visited = [0] * (V + 1)

    for _ in range(E):
        x, y = map(int, input().split())
        node[x].append(y)

    start, goal = map(int, input().split())

    print(f"#{tc} {dfs(start, goal)}")

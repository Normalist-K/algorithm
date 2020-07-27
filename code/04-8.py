import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        idx, edge = map(int, input().split())
        graph[idx].append(edge)

    S, G = map(int, input().split())

    visited = []
    stack = [S]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for i in graph[node]:
                if i not in visited:
                    stack.append(i)

    if G in visited:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")

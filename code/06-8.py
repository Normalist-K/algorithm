import sys

sys.stdin = open("sample_input.txt", "r")


def BFS(graph, S, G, V):
    visited = [False for _ in range(V + 1)]

    queue = []
    count = -1

    queue.append(S)
    while True:
        if len(queue) == 0:
            return 0
        else:
            num_candidates = len(queue)
            count += 1
            for _ in range(num_candidates):
                node = queue.pop(0)
                if node == G:
                    return count
                visited[node] = True

                for candidate in graph[node]:
                    if visited[candidate] == False:
                        queue.append(candidate)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    V, E = map(int, input().split())

    graph = [list() for _ in range(V + 1)]

    for _ in range(0, E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    S, G = map(int, input().split())

    print(graph, S, G, V)
    result = BFS(graph, S, G, V)

    print(f"#{test_case} {result}")

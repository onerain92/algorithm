from collections import deque


def solution(k, x, routes):
    visited = [False] * (len(routes) + 1)
    graph = [[] for _ in range(len(routes) + 1)]

    for route in routes:
        a, b = route
        graph[a].append(b)

    distance = [-1] * (len(routes) + 1)
    distance[x] = 0

    queue = deque([x])
    while queue:
        now = queue.popleft()

        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                queue.append(next_node)

    check = False
    for i in range(1, len(routes) + 1):
        if distance[i] == k:
            return i
            check = True

    if check == False:
        return -1


print(solution(2, 1, [[1, 2], [1, 3], [2, 3], [2, 4]]))

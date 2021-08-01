def solution(n, m, routes, companies):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    x, k = companies

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x == y:
                graph[x][y] = 0

    for route in routes:
        x, y = route
        graph[x][y] = 1
        graph[y][x] = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    distance = graph[1][k] + graph[k][x]
    return -1 if distance >= INF else distance


print(solution(5, 7, [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [4, 5]], [4, 5]))
print(solution(4, 2, [[1, 3], [2, 4]], [3, 4]))

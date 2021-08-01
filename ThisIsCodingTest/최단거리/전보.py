import heapq

def solution(n, start, routes):
    INF = int(1e9)
    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)

    for route in routes:
        start_city, end_city, time = route
        graph[start_city].append((end_city, time))

    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    count = 0
    max_distance = 0
    for d in distance:
        if d != INF:
            count += 1
            max_distance = max(max_distance, d)

    return (count - 1, max_distance)


print(solution(3, 1, [[1, 2, 4], [1, 3, 2]]))

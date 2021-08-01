from collections import deque


# def solution(island, brdige_info, factory):


# print(solution(3, [[1, 2, 2], [3, 1, 3], [2, 3, 2]], [1, 3]))


def bfs(mid):
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True

    while queue:
        x = queue.popleft()

        for y, weight in adjacent[x]:
            if not visited[y] and weight >= mid:
                visited[y] = True
                queue.append(y)

    return visited[end_node]


n, m = list(map(int, input().split(' ')))
adjacent = [[] for _ in range(n + 1)]

min_weight = 1
max_weight = 10

for _ in range(m):
    x, y, weight = list(map(int, input().split(' ')))
    adjacent[x].append((y, weight))
    adjacent[y].append((x, weight))
    min_weight = min(min_weight, weight)
    max_weight = max(max_weight, weight)

start_node, end_node = list(map(int, input().split(' ')))

result = max_weight
while min_weight <= max_weight:
    print(min_weight, max_weight)
    mid = (min_weight + max_weight) // 2

    if bfs(mid):
        result = mid
        min_weight = mid + 1
    else:
        max_weight = mid - 1

print(result)

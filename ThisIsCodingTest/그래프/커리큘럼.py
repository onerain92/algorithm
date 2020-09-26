from collections import deque
import copy

def solution(n, lectures):
    indegree = [0] * (n + 1)
    graph = [[] for i in range(n + 1)]
    time = [0] * (n + 1)

    for i in range(1, n + 1):
        time[i] = lectures[i - 1][0]

        for x in lectures[i - 1][1:-1]:
            indegree[i] += 1
            graph[x].append(i)

    result = copy.deepcopy(time)
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)

    for i in range(1, n + 1):
        print(result[i])


print(solution(5, [[10, -1],
                   [10, 1, -1],
                   [4, 1, -1],
                   [4, 3, 1, -1],
                   [3, 3, -1]]))

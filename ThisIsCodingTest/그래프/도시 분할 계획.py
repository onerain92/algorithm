def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(v, e, routes):
    parent = [0] * (v + 1)
    edges = []
    result = 0

    for i in range(1, v + 1):
        parent[i] = i

    for route in routes:
        house1, house2, cost = route
        edges.append((cost, house1, house2))

    edges.sort()
    last = 0

    for edge in edges:
        cost, house1, house2 = edge

        if find_parent(parent, house1) != find_parent(parent, house2):
            union_parent(parent, house1, house2)
            result += cost
            last = cost

    return result - last


print(solution(7, 12, [[1, 2, 3],
                       [1, 3, 2],
                       [3, 2, 1],
                       [2, 5, 2],
                       [3, 4, 4],
                       [7, 3, 6],
                       [5, 1, 5],
                       [1, 6, 2],
                       [6, 4, 1],
                       [6, 5, 3],
                       [4, 5, 3],
                       [6, 7, 4]]))

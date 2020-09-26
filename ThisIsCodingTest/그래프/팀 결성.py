def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, teams):
    parent = [0] * (n + 1)

    for i in range(n + 1):
        parent[i] = i

    print(parent)

    for team in teams:
        operation, team1, team2 = team
        if operation == 0:
            union(parent, team1, team2)
        elif operation == 1:
            if find_parent(parent, team1) == find_parent(parent, team2):
                print('YES')
            else:
                print('NO')

    print("후: ", parent)


print(solution(7, [[0, 1, 3], [1, 1, 7], [0, 7, 6], [1, 7, 1], [0, 3, 7], [0, 4, 2], [0, 1, 1], [1, 1, 1]]))

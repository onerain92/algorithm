def dfs(n, m, x, y, ice_frame):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if ice_frame[x][y] == 0:
        ice_frame[x][y] = 1

        dfs(n, m, x - 1, y, ice_frame)
        dfs(n, m, x + 1, y, ice_frame)
        dfs(n, m, x, y - 1, ice_frame)
        dfs(n, m, x, y + 1, ice_frame)
        return True
    return False


def solution(n, m, ice_frame):
    result = 0

    for i in range(n):
        for j in range(m):
            if dfs(n, m, i, j, ice_frame) == True:
                result += 1

    return result


print(solution(3, 3, [[0, 0, 1], [0, 1, 0], [1, 0, 1]]))
print(solution(15, 14, [[0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                        [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                        [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
                        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]]))

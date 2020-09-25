from collections import deque

def valid_coord(n, m, x, y):
    return 0 <= x < n and 0 <= y < m

def solution(n, m, maze):
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    queue = deque([(0, 0)])
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current_x, current_y = queue.popleft()

        for direction in DIRECTIONS:
            nx, ny = current_x + direction[0], current_y + direction[1]

            if valid_coord(n, m, nx, ny) and maze[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                maze[nx][ny] = maze[current_x][current_y] + 1
                visited[nx][ny] = True

    return maze[n -1][m -1]


print(solution(5, 6, [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [
      0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
print(solution(3, 3, [[1, 1, 0], [0, 1, 0], [0, 1, 1]]))

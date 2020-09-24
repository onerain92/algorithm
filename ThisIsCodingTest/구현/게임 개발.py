def solution(N, M, location, MAP):
    visited = [[False] * M for _ in range(N)]

    current_x, current_y, current_direction = location
    visited[current_x][current_y] = True
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = 1
    count = 0

    while True:
        current_direction -= 1

        if current_direction == - 1:
            current_direction = 3

        nx, ny = current_x + dx[current_direction], current_y + dy[current_direction]

        if not visited[nx][ny] and MAP[nx][ny] != 1:
            current_x, current_y = nx, ny
            visited[nx][ny] = True
            result += 1
            count = 0

            continue
        else:
            count += 1

        if count == 4:
            nx, ny = current_x - dx[current_direction], current_y - dx[current_direction]

            if MAP[nx][ny] == 1:
                break

            current_x, current_y = nx, ny
            count = 0

    print(result)


print(solution(4, 4, [1, 1, 0], [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]))

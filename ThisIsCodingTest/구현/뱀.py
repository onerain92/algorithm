def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction

def solution(n, apples, direction_info):
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    board = [[0] * (n) for _ in range(n)]
    for apple in apples:
        x, y = apple
        board[x - 1][y - 1] = 1

    cx, cy = 0, 0
    board[cx][cy] = 2
    direction = 0
    time = 0
    index = 0
    queue = [(cx, cy)]

    while True:
        nx, ny = cx + DIRECTIONS[direction][0], cy + DIRECTIONS[direction][1]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx, ny))
                px, py = queue.pop(0)
                board[px][py] = 0

            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                queue.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break

        cx, cy = nx, ny
        time += 1
        if index < len(direction_info) and time == direction_info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, direction_info[index][1])
            index += 1

    return time


print(solution(6, [[3, 4], [2, 5], [5, 3]], [[3, 'D'], [15, 'L'], [17, 'D']]))
print(solution(10, [[1, 2], [1, 3], [1, 4], [1, 5]], [[8, 'D'], [10, 'D'], [11, 'D'], [13, 'L']]))
print(solution(10, [[1, 5], [1, 3], [1, 2], [1, 6], [1, 7]], [[8, 'D'], [10, 'D'], [11, 'D'], [13, 'L']]))

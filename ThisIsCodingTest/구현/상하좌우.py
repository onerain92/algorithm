def solution(N, commands):
    DIRECTIONS = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    current_x, current_y = 1, 1

    for command in commands:
        dx, dy = DIRECTIONS[command]
        nx, ny = current_x + dx, current_y + dy

        if valid_coordinate(N, nx, ny):
            current_x, current_y = nx, ny

    return current_x, current_y

def valid_coordinate(N, x, y):
    return 1 <= x <= N and 1 <= y <= N


print(solution(5, ["R", "R", "R", "U", "D", "D"]))

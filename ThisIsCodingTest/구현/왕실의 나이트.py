def solution(location):
    DIRECTIONS = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1) ,(2, 1) ,(1, -2) ,(1, 2)]
    x, y = int(ord(location[0])) - int(ord('a')) + 1, int(location[1])
    count = 0

    for direction in DIRECTIONS:
        dx, dy = direction
        nx, ny = x + dx, y + dy

        if vaild_coordinate(nx, ny):
            count += 1

    return count


def vaild_coordinate(x, y):
    return 1 <= x < 9 and 1<= y < 9

print(solution("c2"))

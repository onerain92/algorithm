def solution(coordinates):
    coordinates.sort()

    return coordinates


print(solution([(3, 4), (1, 1), (1, -1), (2, 2), (3, 3)]))

def solution2(coordinates):
    array = []

    for coordinate in coordinates:
        x, y = coordinate
        array.append((x, y))

    array = sorted(array)

    for i in array:
        print(i[0], i[1])


print(solution2([[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]))

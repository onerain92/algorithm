def solution(n, m, cards):
    row_min = 0
    max_value = 0

    for card in cards:
        row_min = min(card)

        if max_value < row_min:
            max_value = row_min

    return max_value


print(solution(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]]))
print(solution(2, 4, [[7, 3, 1, 8], [3, 3, 3, 4]]))

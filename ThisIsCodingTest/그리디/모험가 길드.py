def solution(n, adventurers):
    adventurers.sort()
    result = 0
    count = 0

    for adventurer in adventurers:
        count += 1
        if count >= adventurer:
            result += 1
            count = 0

    return result


print(solution(5, [2, 3, 1, 2, 2]))

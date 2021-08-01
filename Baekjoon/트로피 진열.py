def solution(trophys):
    left = 1
    right = 1

    for i in range(1, len(trophys)):
        if trophys[i] - trophys[i - 1] > 0:
            left += 1
        else:
            right += 1

    return left, right


print(solution([1, 2, 3, 4, 5]))


def ascending(trophys):
    now = trophys[0]
    result = 1

    for i in range(1, len(trophys)):
        if now < trophys[i]:
              result += 1
              now = trophys[i]

    return result

def solution2(trophys):
    print(ascending(trophys))
    trophys.reverse()
    print(ascending(trophys))

print(solution2([1, 2, 3, 4, 5]))

def solution(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1

        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1

        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1

        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1

        return

    solution(n / 2, x, y)
    solution(n / 2, x, y + n / 2)
    solution(n / 2, x + n / 2, y)
    solution(n / 2, x + n / 2, y + n / 2)

result = 0
N, X, Y = map(int, input().split(' '))
print(solution(2 ** N, 0, 0))

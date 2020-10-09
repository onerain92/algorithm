import itertools


def solution(money):
    sum_array = set()
    for i in range(1, len(money) + 1):
        combinations = itertools.combinations(money, i)

        for combination in combinations:
            sum_array.add(sum(combination))

    sum_array = list(sum_array)
    for i in range(len(sum_array)):
        if i + 1 != sum_array[i]:
            return i + 1


print(solution([3, 2, 1, 1, 9]))
print(solution([3, 5, 7]))

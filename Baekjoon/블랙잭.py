import itertools

def solution(card_num, max_num, cards):
    all_cases = itertools.combinations(cards, 3)
    max_sum = 0

    for case in all_cases:
        case_sum = sum(case)
        if case_sum <= max_num and case_sum > max_sum:
            max_sum = case_sum

    return max_sum

print(solution(5, 21, [5, 6, 7, 8, 9]))

def solution2():
    n, m = list(map(int, input().split(' ')))
    data = list(map(int, input().split(' ')))

    result = 0
    length = len(data)

    for i in range(0, length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                sum_value = data[i] + data[j] + data[k]

                if sum_value <= m:
                    result = max(result, sum_value)

    print(result)

solution2()

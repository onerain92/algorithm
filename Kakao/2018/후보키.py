from itertools import chain, combinations


def get_all_subset(iterable):
    s = list(iterable)

    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def get_all_unique_subset(relations):
    subset_list = get_all_subset(list(range(0, len(relations[0]))))
    unique_list = []

    for subset in subset_list:
        unique = True
        row_set = set()

        for i in range(len(relations)):
            row = ''

            for j in subset:
                row += relations[i][j] + '.'

            if row in row_set:
                unique = False
                break
            row_set.add(row)
        if unique:
            unique_list.append(subset)

    return unique_list


def solution(relations):
    unique_list = get_all_unique_subset(relations)
    unique_list = sorted(unique_list, key=lambda x: len(x))
    ansewr_list = []

    for subset in unique_list:
        subset = set(subset)
        check = True

        for j in ansewr_list:
            if j.issubset(subset):
                check = False
        if check == True:
            ansewr_list.append(subset)

    return len(ansewr_list)


print(solution([["100", "ryan", "music", "2"], ["200", "appeach", "math", "2"], ["300", "tube", "computer", "3"], [
      "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "appeach", "music", "2"]]))

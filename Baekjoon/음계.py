# https://www.acmicpc.net/problem/2920

def solution1(scales):
    scale_diffrences = []

    for i in range(1, len(scales)):
        scale_diffrences.append(int(scales[i]) - int(scales[i - 1]))

    total = sum(scale_diffrences)

    if total == 7:
        return 'ascending'
    elif total == -7:
        return 'descending'
    else:
        return 'mixed'


def solution2(scales):
    scales = list(map(int, input().split(' ')))

    asc = True
    desc = True

    for i in range(1, len(scales)):
        if scales[i] < scales[i - 1]:
            asc = False
        elif scales[i] > scales[i - 1]:
            desc = False

    if asc:
        print('ascending')
    elif desc:
        print('descending')
    else:
        print('mixed')


print(solution2('12345678'))
print(solution2('87654321'))
print(solution2('81726354'))

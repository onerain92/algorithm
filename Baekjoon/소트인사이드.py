# https://www.acmicpc.net/problem/1427

def solution(num):
    num_array = list(num)
    num_array.sort(reverse=True)

    return ''.join(num_array)


print(solution('2143'))

def solution2(num):
    for i in range(9, -1, -1):
        for j in num:
            if int(j) == i:
                print(i, end='')

print(solution2('2143'))

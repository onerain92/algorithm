def solution(save_data, find_data):
    data_set = set(save_data)
    answer = []

    for data in find_data:
        if data in data_set:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([4, 1, 5, 2, 3], [1, 3, 7, 9, 5]))

def solution2():
    n = int(input())
    data_set = set(map(int, input().split(' ')))
    m = int(input())
    find_data = list(map(int, input().split(' ')))

    for data in find_data:
        if data in data_set:
            print(1)
        else:
            print(0)

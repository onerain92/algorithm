def solution(n, arr):
    array = sorted(arr, key=lambda x: x[1])

    result = ' '.join(map(lambda x: x[0], array))
    return result


print(solution(2, [['홍길동', 95], ['이순신', 77]]))

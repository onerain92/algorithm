def solution(N, M, K, arr):
    arr.sort(reverse=True)
    first_value = arr[0]
    second_value = arr[1]
    result = 0

    while True:
        for i in range(K):
            if M == 0:
                break
            result += first_value
            M -= 1

        if M == 0:
            break;

        result += second_value
        M -= 1

    return result


print(solution(5, 8, 3, [2, 4, 5, 4, 6]))

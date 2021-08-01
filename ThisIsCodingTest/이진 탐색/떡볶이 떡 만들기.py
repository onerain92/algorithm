def solution(number_of_tteok, tteok_length, tteok_heights):
    tteok_heights.sort()
    start = 0
    end = max(tteok_heights)

    result = 0
    while start <= end:
        total_length = 0
        mid = (start + end) // 2

        for tteok in tteok_heights:
            if tteok > mid:
                total_length += tteok - mid

        if total_length < tteok_length:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result


print(solution(4, 6, [19, 15, 10, 17]))

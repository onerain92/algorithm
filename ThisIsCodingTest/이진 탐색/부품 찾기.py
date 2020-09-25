def binary_search(shop_parts, parts, start, end):
    while start <= end:
        mid = (start + end) // 2

        if shop_parts[mid] == parts:
            return 'yes'
        elif shop_parts[mid] > parts:
            end = mid - 1
        else:
            start = mid + 1

    return 'no'


def solution(shop_parts, guest_parts):
    result = []
    shop_parts.sort()

    for parts in guest_parts:
        start = 0
        end = len(shop_parts) - 1
        result.append(binary_search(shop_parts, parts, start, end))

    return ' '.join(result)


print(solution([8, 3, 7, 9, 2], [5, 7, 9]))

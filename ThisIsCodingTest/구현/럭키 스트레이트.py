# def solution(n):
#     n = str(n)
#     arr = list(n)
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     left_total = 0
#     right_total = 0

#     for el in left:
#         left_total += int(el)

#     for el in right:
#         right_total += int(el)

#     if left_total == right_total:
#         return 'LUCKY'
#     else:
#         return 'READY'


# print(solution(123402))
# print(solution(7755))


def solution(n):
    n = str(n)
    length = len(n)
    summary = 0

    for i in range(length // 2):
        summary += int(n[i])

    for i in range(length // 2, length):
        summary -= int(n[i])

    if summary == 0:
        return 'LUCKY'
    else:
        return 'READY'


print(solution(123402))
print(solution(7755))

def solution(locations, N):
    answer = 0
    locations.sort()
    lower = locations[1] - locations[0]
    upper = locations[-1] - locations[0]

    while lower <= upper:
        mid = (lower + upper) // 2
        value = locations[0]
        count = 1

        for i in range(1, len(locations)):
            if value + mid <= locations[i]:
                count += 1
                value = locations[i]

        if count >= N:
            lower = mid + 1
            answer = mid
        else:
            upper = mid - 1

    return answer

print(solution([1, 2, 8, 4, 9], 3))

# n, c = list(map(int, input().split(' ')))
# locations = []

# for _ in range(n):
#     locations.append(int(input()))

# locations.sort()
# answer = 0
# lower = locations[1] - locations[0]
# upper = locations[-1] - locations[0]

# while lower <= upper:
#     mid = (lower + upper) // 2
#     value = locations[0]
#     count = 1

#     for i in range(1, len(locations)):
#         if value + mid <= locations[i]:
#             count += 1
#             value = locations[i]

#     if count >= c:
#         lower = mid + 1
#         answer = mid
#     else:
#         upper = mid - 1

# print(answer)

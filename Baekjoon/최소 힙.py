import heapq

n = int(input())
array = []
result = []

for _ in range(n):
    value = int(input())

    if value == 0:
        if array:
            result.append(heapq.heappop(array))
        else:
            result.append(0)
    else:
        heapq.heappush(array, value)

for data in result:
    print(data)

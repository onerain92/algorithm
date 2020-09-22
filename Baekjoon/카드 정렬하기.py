import heapq

n = int(input())
heap = []
answer = 0

for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

while len(heap) != 1:
    data1 = heapq.heappop(heap)
    data2 = heapq.heappop(heap)
    sum_data = data1 + data2
    answer += sum_data
    heapq.heappush(heap, sum_data)

print(answer)

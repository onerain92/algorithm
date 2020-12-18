from collections import deque

N = int(input())
queue = deque()

for i in range(1, N + 1):
  queue.append(i)

while queue:
  if len(queue) == 1:
    break
  queue.popleft()
  next_card = queue.popleft()
  queue.append(next_card)

print(queue.popleft())

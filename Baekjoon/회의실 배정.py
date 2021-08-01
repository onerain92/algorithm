N = int(input())
meetings = []
count = 0
end_time = 0

for _ in range(N):
  start, end = map(int, input().split())
  meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

for i in range(len(meetings)):
  if end_time <= meetings[i][0]:
    end_time = meetings[i][1]
    count += 1

print(count)

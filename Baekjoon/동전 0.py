N, K = map(int, input().split())
coins = []
count = 0

for _ in range(N):
  coin = int(input())
  coins.append(coin)

coins.sort(reverse=True)

for coin in coins:
  if coin <= K:
    count += K // coin
    K = K % coin

print(count)

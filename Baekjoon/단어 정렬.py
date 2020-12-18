N = int(input())
words = []

for _ in range(N):
  word = input()
  words.append((word, len(word)))

words = list(set(words))
words.sort(key=lambda x: (x[1], x[0]))

for word in words:
  print(word[0])

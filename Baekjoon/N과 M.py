from itertools import permutations

N, M = map(int, input().split())
combi = permutations(range(1, N+1), M)

for i in combi:
    print(' '.join(map(str, i)))

def solution(N):
    storage = [0] * (N + 1)
    storage[1] = 1
    storage[2] = 2

    for i in range(3, N + 1):
        storage[i] = storage[i - 1] + storage[i - 2] % 15746

    return storage[N]


print(solution(4))

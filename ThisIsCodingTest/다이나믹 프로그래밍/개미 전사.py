def solution(n, warehouse):
    dp = [0] * 100
    dp[0] = warehouse[0]
    dp[1] = max(warehouse[0], warehouse[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + warehouse[i])

    return dp[n - 1]


print(solution(4, [1, 3, 1, 5]))

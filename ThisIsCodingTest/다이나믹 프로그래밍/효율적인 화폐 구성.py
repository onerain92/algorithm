def solution(n, m, monetarys):
    dp = [10001] * (m + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(monetarys[i], m + 1):
            if dp[j - monetarys[i]] != 10001:
                dp[j] = min(dp[j], dp[j - monetarys[i]] + 1)

    if dp[m] == 10001:
        return -1
    else:
        return dp[m]


print(solution(2, 15, [2, 3]))
print(solution(3, 7, [2, 3, 5]))
print(solution(3, 4, [3, 5, 7]))

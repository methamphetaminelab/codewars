def exp_sum(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for num in range(1, n + 1):
        for i in range(num, n + 1):
            dp[i] += dp[i - num]

    return dp[n]
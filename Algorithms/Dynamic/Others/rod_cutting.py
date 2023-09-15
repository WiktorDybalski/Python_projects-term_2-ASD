# Typical rod cutting problem algorythm
cost_of_cut = [(3, 3), (1, 1), (5, 8), (7, 12)]
X = 18


def rod_cutting(cost_of_cut, x):
    nc = len(cost_of_cut)
    dp = [0 for _ in range(x + 1)]
    cuts = [[] for _ in range(x + 1)]
    for i in range(nc):
        cut = cost_of_cut[i][0]
        cost = cost_of_cut[i][1]
        dp[cut] = cost
        cuts[cut] = [cost]
    for i in range(1, x + 1):
        for j in range(1, i):
            if dp[i] < dp[j] + dp[i - j]:
                dp[i] = dp[j] + dp[i - j]
                cuts[i] = cuts[j] + cuts[i - j]
    return dp, cuts


print(rod_cutting(cost_of_cut, X))

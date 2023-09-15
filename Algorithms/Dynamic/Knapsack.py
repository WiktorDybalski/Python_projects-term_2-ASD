# Finding items that toegether have the wage under the B and have the maximum prize

def Knapsack(W, P, B):
    n = len(W)
    F = [[0 for b in range(B + 1)] for i in range(n)]
    for b in range(W[0], B + 1):
        F[0][b] = P[0]
    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])
    for i in range(len(F)):
        print(F[i])
    return F[n - 1][B]


W = [2, 3, 4, 5]
P = [3, 4, 5, 6]
B = 8

print(Knapsack(W, P, B))


def Plecak(W, P, B):
    nw = len(W)
    wages = [[0 for _ in range(B + 1)] for c in range(nw + 1)]
    for i in range(W[0], B + 1):
        wages[1][i] = P[0]
    for wage in range(W[0], B + 1):
        for items in range(2, nw + 1):
            wages[items][wage] = wages[items - 1][wage]
            if wage - W[items - 1] >= 0:
                wages[items][wage] = max(wages[items][wage], wages[items - 1][wage - W[items - 1]] + P[items - 1])
    for i in range(len(wages)):
        print(wages[i])
    return wages[nw][B]


print(Plecak(W, P, B))

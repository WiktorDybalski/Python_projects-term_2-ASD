from egz2btesty import runtests

inf = float("inf")


def magic(C):
    n = len(C)
    dp = [0 for _ in range(n)]
    for room in range(n - 1):
        chest = C[room][0]
        for doors in range(1, 4):
            if C[room][doors][1] == -1:
                continue
            if chest > C[room][doors][0]:
                hand = min(10, chest - C[room][doors][0])
                if hand + C[room][doors][0] < chest:
                    hand = -inf
            else:
                hand = chest - C[room][doors][0]
            to_room = C[room][doors][1]
            dp[to_room] = max(dp[to_room], dp[room] + hand)
    return dp[n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)

# Find a day and a amount of people who give a message
def BFS_modd(G, s, t):
    n = len(G)
    max_cnt = 0
    max_d = 0
    temp = 0
    v = 0
    cnt = 0
    visited = [False] * n
    d = [-1] * n
    parrent = [None] * n
    queue = []

    queue.append(s)
    visited[s] = True
    d[s] = 0
    parrent[0] = None

    while queue:
        u = queue.pop(0)
        if d[u] != temp:
            cnt = 0
        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                d[v] = d[u] + 1
                parrent[v] = u
                cnt += 1
                temp = d[u]
        if max_cnt < cnt:
            max_cnt = cnt
            max_d = d[u] + 1
    return max_d, max_cnt


def text(G, v, t):
    result = BFS_modd(G, v, t)
    print("Po ilu dniach:", result[0])
    print("Ile osób:", result[1])


G = [[1], [0, 2, 4], [1, 3, 5], [2, 4, 6], [1, 3, 7, 8], [2], [3], [4], [8]]
(text(G, 0, 6))

lakes = [["L", "W", "L", "L", "L", "L", "L", "L"],
         ["L", "W", "L", "W", "W", "L", "L", "L"],
         ["L", "L", "L", "W", "W", "L", "W", "L"],
         ["L", "W", "W", "W", "W", "L", "W", "L"],
         ["L", "L", "W", "W", "L", "L", "L", "L"],
         ["L", "W", "L", "L", "L", "L", "W", "W"],
         ["W", "W", "L", "W", "W", "L", "W", "L"],
         ["L", "L", "L", "W", "L", "L", "L", "L"]]


# How many lakes are there in the matrix?

def DFS1(G, visited, queue):
    def DFS_Visit(G, vi, vj, moves):
        n = len(G)
        visited[vi][vj] = True
        for move in moves:
            i = vi + move[0]
            j = vj + move[1]
            if (n - 1) >= i >= 0 and (n - 1) >= j >= 0 and not visited[i][j] and G[i][j] == "W":
                DFS_Visit(G, i, j, moves)

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    amount_of_lakes = 0
    while queue:
        (vi, vj) = queue.pop(0)
        if not visited[vi][vj]:
            amount_of_lakes += 1
            DFS_Visit(G, vi, vj, moves)
    return amount_of_lakes


def how_many(lakes):
    n = len(lakes)
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = []
    for i in range(n):
        for j in range(n):
            if lakes[i][j] == "W":
                queue.append((i, j))
    how_many_lakes = DFS1(lakes, visited, queue)
    return how_many_lakes


# How many cells are in the biggest lake?
def DFS2(G, visited, queue):
    def DFS_Visit(G, vi, vj, moves):
        nonlocal big
        n = len(G)
        big += 1
        visited[vi][vj] = True
        for move in moves:
            i = vi + move[0]
            j = vj + move[1]
            if (n - 1) >= i >= 0 and (n - 1) >= j >= 0 and not visited[i][j] and G[i][j] == "W":
                DFS_Visit(G, i, j, moves)
        return big

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    amount_of_lakes = 0
    the_biggest = 0
    while queue:
        (vi, vj) = queue.pop(0)
        if not visited[vi][vj]:
            amount_of_lakes += 1
            big = 0
            big = DFS_Visit(G, vi, vj, moves)
            the_biggest = max(the_biggest, big)
    return the_biggest


def the_biggest_lake(lakes):
    n = len(lakes)
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = []
    for i in range(n):
        for j in range(n):
            if lakes[i][j] == "W":
                queue.append((i, j))
    the_biggest = DFS2(lakes, visited, queue)
    return the_biggest


# Is it possible to get from (0, 0) to (n-1, n-1) without crossing any lake?
def DFS3(G, visited, i, j):
    def DFS_Visit(G, vi, vj, moves):
        nonlocal possible
        n = len(G)
        visited[vi][vj] = True
        if vi == n - 1 and vj == n - 1:
            possible = True
            return True
        for move in moves:
            i = vi + move[0]
            j = vj + move[1]
            if (n - 1) >= i >= 0 and (n - 1) >= j >= 0 and not visited[i][j] and G[i][j] == "L":
                DFS_Visit(G, i, j, moves)
        return possible

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    possible = False
    DFS_Visit(G, i, j, moves)
    if possible:
        return True
    return False


# The shortest path from (0, 0) to (n-1, n-1) without crossing any lake
def is_it_possible(lakes):
    n = len(lakes)
    visited = [[False for _ in range(n)] for _ in range(n)]
    is_it = DFS3(lakes, visited, 0, 0)
    return is_it


def BFS(G, visited, d, vi, vj):
    n = len(G)
    queue = [(vi, vj)]
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        vi, vj = queue.pop(0)

        for move in moves:
            i = vi + move[0]
            j = vj + move[1]
            if (n - 1) >= i >= 0 and (n - 1) >= j >= 0 and not visited[i][j] and G[i][j] == "L":
                queue.append((i, j))
                visited[i][j] = True
                d[i][j] = d[vi][vj] + 1
    return d


def the_shortest_path(lakes):
    n = len(lakes)
    visited = [[False for _ in range(n)] for _ in range(n)]
    d = [[0 for _ in range(n)] for _ in range(n)]
    d = BFS(lakes, visited, d, 0, 0)
    print(d)
    return d[n - 1][n - 1]


print(how_many(lakes))
print(the_biggest_lake(lakes))
print(is_it_possible(lakes))
print(the_shortest_path(lakes))

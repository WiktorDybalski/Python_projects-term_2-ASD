# Algorythm known as strongly connected components
# zlozonosc to O(V+E), gdzie V to liczba wierzcholkow a E to liczba krawedzi w grafie

def kosaraju(graph):
    def dfs1(node):
        visited[node] = True
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs1(neighbor)
        stack.append(node)

    def dfs2(node, component):
        visited[node] = True
        component.append(node)
        if node in reversed_graph:
            for neighbor in reversed_graph[node]:
                if neighbor not in visited:
                    dfs2(neighbor, component)

    visited = set()
    stack = []
    scc_list = []

    # First DFS pass to fill the stack
    for node in graph:
        if node not in visited:
            dfs1(node)

    # Create the reversed graph
    reversed_graph = {}
    for node in graph:
        if node not in reversed_graph:
            reversed_graph[node] = []
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in reversed_graph:
                    reversed_graph[neighbor] = []
                reversed_graph[neighbor].append(node)

    visited.clear()

    # Second DFS pass to find SCCs
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs2(node, component)
            scc_list.append(component)

    return scc_list


def create_new_graph(scc_list, graph):
    new_graph = {}
    added_sccs = set()

    for scc in scc_list:
        scc_neighbors = set()
        for node in scc:
            if node in graph:
                for neighbor in graph[node]:
                    for other_scc in scc_list:
                        if neighbor in other_scc and scc != other_scc:
                            scc_neighbors.add(tuple(other_scc))

        new_graph[tuple(scc)] = list(scc_neighbors)

    return new_graph


# Example usage:
graph = {
    0: [1, 4, 2],
    1: [0],
    2: [1]
}

scc_list = kosaraju(graph)
new_graph = create_new_graph(scc_list, graph)
print(new_graph)

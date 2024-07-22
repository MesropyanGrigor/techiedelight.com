def bfs(graph, start):
    traversal_order = []

    visited=set([start])

    queue = [start]

    while queue:

        node = queue.pop(0)

        traversal_order.append(node)

        for nn in graph[node]:
            if nn not in visited:
                visited.add(nn)
                queue.append(nn)

    return len(graph.keys()) == len(visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

start_node = 'A'
print("BFS Traversal Order:", bfs(graph, start_node))
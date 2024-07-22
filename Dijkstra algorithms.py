
def dijkstra(graph, start):
    # Initialize distances with infinity and start node with distance 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Track visited nodes
    visited = set()
    
    while len(visited) < len(graph):
        # Find the node with the minimum distance that is not yet visited
        min_node = None
        for node in graph:
            if node not in visited and (min_node is None or distances[node] < distances[min_node]):
                min_node = node
        
        # Mark the selected node as visited
        visited.add(min_node)
        
        # Update distances for neighbors of the selected node
        for neighbor, weight in graph[min_node].items():
            if neighbor not in visited:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print("Shortest paths from node A:", shortest_paths)



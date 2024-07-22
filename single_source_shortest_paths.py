'''

Given a weighted directed graph with non-negative edge weights and a source vertex, return the shortest path cost from the source vertex to every other reachable vertex in the graph.

Input: Graph [edges = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7), (4, 1, 1), (4, 2, 8), (4, 3, 2)], n = 5], source = 0
Here, tuple (x, y, w) represents an edge from x to y having weight w.

Output: {(0, 4, 4), (0, 4, 6), (0, 4, 5), (0, 4, 3)}
Here, tuple (s, d, c) indicates that the shortest path from source s to destination d has cost c.

Explanation:

• Shortest path from (0 —> 1) is [0 —> 4 —> 1] with cost 4.
• Shortest path from (0 —> 2) is [0 —> 4 —> 1 —> 2] with cost 6.
• Shortest path from (0 —> 3) is [0 —> 4 —> 3] with cost 5.
• Shortest path from (0 —> 4) is [0 —> 4] with cost 3.

Input: Graph [edges = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7), (4, 1, 1), (4, 2, 8), (4, 3, 2)], n = 5], source = 1
Output: {(1, 2, 2), (1, 3, 6), (1, 4, 4)}
Explanation:

• Shortest path from (1 —> 0) does not exist.
• Shortest path from (1 —> 2) is [1 —> 2] with cost 2.
• Shortest path from (1 —> 3) is [1 —> 4 —> 3] with cost 6.
• Shortest path from (1 —> 4) is [1 —> 4] with cost 4.

Constraints:

• The graph is implemented using an adjacency list.
• The maximum number of nodes in the graph is 100, i.e., 0 <= n < 100, and each node is represented by its numeric value.
• The source vertex is among the set of vertices in the graph.

'''

class Solution:

	'''
	# Definition for a Graph
	class Graph:
		def __init__(self, edges=None, n=0):

			# Total number of nodes in the graph
			self.n = n

			# List of lists to represent an adjacency list
			self.adjList = [[] for _ in range(n)]

			# add edges to the directed graph
			for (source, dest, weight) in edges:
				self.adjList[source].append((dest, weight))
	'''

	def findShortestPaths(self, graph: Graph, source: int) -> Set[Tuple[int]]:
		# Write your code here...
		distances = {node: float("inf") for node in range(graph.n)}
		distances[source] = 0 
		
		visited = set()
		
		while len(visited) < graph.n:
			min_node = None
			for node in range(graph.n):
				if node not in visited and (min_node is None or distances[node] < distances[min_node]):
					min_node = node
					
			visited.add(min_node)
			print(visited)
			for neighbor, weight in graph.adjList[min_node]:
				
				if neighbor not in visited:
					#visited.add(neighbor)
					new_distance = distances[min_node] + weight
					
					if new_distance < distances[neighbor]:
						distances[neighbor] = new_distance
		
	#	print(distances)
		result = set()
		for node, weight in distances.items():
			if weight != float("inf") and node != source:
				result.add((source, node, weight))
		
		#result = {(source, node, weight) for node, weight in distances.items() if node != source}

				
		return result


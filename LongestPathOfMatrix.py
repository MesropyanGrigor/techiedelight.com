'''

Given a rectangular path in the form of a binary matrix, find the length of the longest possible route from source to destination by moving to only non-zero adjacent positions, i.e., A route can be formed from positions having their value as 1. Note there should not be any cycles in the output path.

Input:

matrix = [
	[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
	[1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
	[1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
	[1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
]
src  = (0, 0)
dest = (5, 7)

Output: 22

Explanation: The longest path is:

(0, 0) —> (1, 0) —> (2, 0) —> (2, 1) —> (2, 2) —> (1, 2) —> (0, 2) —> (0, 3) —> (0, 4) —> (1, 4) —> (1, 5) —> (2, 5) —> (2, 4) —> (3, 4) —> (4, 4) —> (5, 4) —> (5, 5) —> (5, 6) —> (4, 6) —> (4, 7) —> (4, 8) —> (5, 8) —> (5, 7)

Note: The solution should return 0 if no path is possible.

'''



class Node:
	def __init__(self, coords, value, paths = []):
		self.coords = coords
		self.value = value
		self.paths = []
		self.paths.extend(paths)
		self.paths.append(coords)

class Solution:
	def findLongestPath(self, mat: List[List[int]], src: Tuple[int], dest: Tuple[int]) -> int:
		print("right")
		paths = []
		visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
		
		#if dest[0] > src[0] or dest[1] > src[1]:
		#	return 0
		
		#if src == dest:
	#		return 0
		
		if mat[src[0]][src[1]] == 0:
			return 0
			
		queues = [Node(src, 0)]
		
		while queues:
			node = queues.pop()
			
			if node.coords == dest:
				paths.append(node)
				
			coords = node.coords
				
			if self.is_valid(coords[0] -1, coords[1], mat, visited) and (coords[0] -1, coords[1]) not in node.paths:
				queues.append(
					Node(
						(coords[0] -1, coords[1]), node.value + 1, node.paths,
						)
					)
				
			if self.is_valid(coords[0] + 1, coords[1], mat, visited) and (coords[0] + 1, coords[1]) not in node.paths:
				queues.append(
					Node(
						(coords[0] + 1, coords[1]), node.value + 1, node.paths,
						)
					)
				
			if self.is_valid(coords[0], coords[1] - 1, mat, visited) and (coords[0], coords[1] - 1) not in node.paths:
				queues.append(
					Node(
						(coords[0], coords[1] - 1), node.value + 1, node.paths,
						)
					)
				
			if self.is_valid(coords[0], coords[1] + 1, mat, visited) and (coords[0], coords[1] + 1) not in node.paths:
				queues.append(
					Node(
						(coords[0], coords[1] + 1), node.value + 1, node.paths,
						)
					)
			
		values = [node.value for node in paths]
		#pprint.pprint(values)
		#pprint.pprint(visited)
		return max(values) if values else 0
				
			
				
		
	def is_valid(self, x, y, mat, visited):
		if x >= 0 and y >= 0 and x < len(mat) and y < len(mat[0]) and mat[x][y] == 1:# and not visited[x][y]:
			visited[x][y] = True
			return True
		return False
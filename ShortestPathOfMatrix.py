'''

Given a maze in the form of a binary rectangular matrix, find the length of the shortest path from a given source to a given destination. The path can only be constructed out of cells having value 1, and at any moment, you can only move one step in one of the four directions (Top, Left, Down, Right).

Input:

matrix = [
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
	[1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
	[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
src  = (0, 0)
dest = (5, 7)

Output: 12

Explanation: The shortest path from (0, 0) to (5, 7) has length 12. The shortest path is marked below with x.

[
	[x, x, x, x, x, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, x, 1, 0, 1, 0, 1],
	[0, 0, 1, 0, x, x, x, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, x, x, 0, 1],
	[0, 0, 0, 1, 0, 0, 0, x, 0, 1],
	[1, 0, 1, 1, 1, 0, 0, x, 1, 0],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]

Note: The solution should return -1 if no path is possible.

'''

class Solution:
	def findShortestPath(self, mat: List[List[int]], src: Tuple[int], dest: Tuple[int]) -> int:
		print("right")
		visitied_state = [[ False for _ in range(len(mat[0]))] for _ in range(len(mat))]
		
		if mat[src[0]][src[1]] == 0:
			return -1
		
		queue = [(src, 0)]
		visitied_state[src[0]][src[1]] = True
		
		while queue:
			source = queue.pop(0)
			coords = source[0]
			print(coords, "===", dest)
			if coords == dest:
				return  source[1]
			
			# moving up	
			if self.is_valid(coords[0] - 1, coords[1], mat, visitied_state):
				queue.append(((coords[0] - 1, coords[1]), source[1] + 1))
				
			# moving down
			if self.is_valid(coords[0] + 1, coords[1], mat, visitied_state):
				queue.append(((coords[0] + 1, coords[1]), source[1] + 1))
				
			# moving left
			if self.is_valid(coords[0], coords[1] - 1, mat, visitied_state):
				queue.append(((coords[0], coords[1] - 1), source[1] + 1))
				
			
			# moving right
			if self.is_valid(coords[0], coords[1] + 1, mat, visitied_state):
				queue.append(((coords[0], coords[1] + 1), source[1] + 1))
			
		return -1
				
				
				
				
			
	def is_valid(self, x, y, grid, visited):
		if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == 1 and not visited[x][y]:
			visited[x][y] = True
			return True
		return False
		

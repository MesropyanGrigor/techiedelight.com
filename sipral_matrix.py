'''

Given a positive number `N`, return an `N × N` spiral matrix containing numbers from 1 to `N × N` in a counterclockwise direction.

Input: N = 5

Output:
[
	[25, 24, 23, 22, 21],
	[10, 9,  8,  7,  20],
	[11, 2,  1,  6,  19],
	[12, 3,  4,  5,  18],
	[13, 14, 15, 16, 17]
]

'''

class Solution:
	def findSpiralOrder(self, N: int):
		mat = []
		if N <= 0:
			return mat
			
		for i in range(N):
			mat.append([0]*N)
			
		value = N*N	
		
		left = 0 
		right = N
		top = 0 
		bottom = N
		
		while value != 0:
			
			for i in range(left, right):
				mat[top][i] = value
				value -= 1
				if not value:
					return mat
				
			top = top + 1

			
			for j in range(top, bottom):
				mat[j][right - 1] = value
				value -= 1
				if not value:
					return mat				
			
			right = right - 1 

			for i in range(right - 1, left - 1, -1):
				mat[bottom - 1][i] = value
				value = value - 1 
				if not value:
					return mat
				
			bottom = bottom - 1 
			
			for i in range(bottom - 1, top -1, -1):
				mat[i][left] = value
				value = value - 1 
				if not value:
					return mat			
			left += 1
		return mat
		

ss = Solution()
for row in ss.findSpiralOrder(5):
	print(row)
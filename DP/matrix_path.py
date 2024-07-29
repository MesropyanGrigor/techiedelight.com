'''

Given an `M × N` integer matrix where each cell has a non-negative cost associated with it, count the number of paths to reach the last cell (M-1, N-1) of the matrix from its first cell (0, 0) such that the path has given cost. You can only move one unit right or one unit down from any cell, i.e., from cell (i, j), you can move to (i, j+1) or (i+1, j).

Input:

mat = [
	[4, 7, 1, 6],
	[5, 7, 3, 9],
	[3, 2, 1, 2],
	[7, 1, 6, 3]
]

cost: 25

Output: 2

Explanation: The following two paths have a cost of 25.


	4 — 7 — 1   6				4   7   1   6
			|					|
	5   7   3   9				5 — 7 — 3   9
			|							|
	3   2   1   2				3   2   1 — 2
			|								|
	7   1   6 — 3				7   1   6   3

'''
import sys
sys.setrecursionlimit(12000)

def check(mat, i, j, dp=[], size=0):
	if i == len(mat) - 1 and j == len(mat[0]) - 1:
		dp.append(size + mat[i][j])
		return
	elif i < len(mat) and j < len(mat[0]):
		size = size + mat[i][j]
	else:
		return
	

	check(mat, i + 1, j, dp, size)
	check(mat, i, j + 1, dp, size)
		


mat = [
	[4, 7, 1, 6],
	[5, 7, 3, 9],
	[3, 2, 1, 2],
	[7, 1, 6, 3]
]

values =[]

check(mat, 0, 0, values)

print(values.count(25))
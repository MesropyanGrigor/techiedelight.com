'''

Given a positive integer n, return all n–digit binary numbers without any consecutive 1's.

Input: n = 5
Output: {'00000', '00001', '00010', '00100', '00101', '01000', '01001', '01010', '10000', '10001', '10010', '10100', '10101'}

'''

def get_combos(n):
	results = set()
	base = [0 for _ in range(n)]
	results.add(''.join(str(vv) for vv in base))
	def backtracking(st):
		print(base)
		if '11' not in ''.join(str(vv) for vv in base):
			results.add(''.join(str(vv) for vv in base))
			
		for i in range(st, n):
			base[i] = 1
			backtracking(i+2)
			base[i] = 0 
		
	backtracking(0)	
	return results
	
	
	

class Solution:
	def findNDigitNumbers(self, n: int) -> Set[str]:
		# Write your code here...
		return get_combos(n)


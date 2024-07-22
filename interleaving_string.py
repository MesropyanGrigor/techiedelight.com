class Solution:
	def isInterleaving(self, X: str, Y: str, S: str) -> bool:
		if not X:
			return Y == S
		if not Y:
			return X == S
			
		x_map = {}
		y_map = {}
		new_S = ""
		previous = 0
		for i in range(0, len(X)):
			if not previous:
				index = S.find(X[i])
				previous = index
			else:
				index = S[previous+1:].find(X[i])
				#print(S[previous+1:])
				
				#print(index,"===", X[i])
				if index == -1:
					return False
				previous = index


		#print("second")
		previous = 0
		for i in range(0, len(Y)):
			if not previous:
				index = S.find(Y[i])
				previous = index
			else:
				#print(S[previous+1:])
				index = S[previous+1:].find(Y[i])
				if index == -1:
					return False
				previous = index
		
		#print("true")
		return True


ss = Solution()

print(ss.isInterleaving('AB', 'CD', 'ACDE'))
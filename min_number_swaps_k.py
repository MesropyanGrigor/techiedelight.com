'''

Given string representation of a positive integer, find the minimum number possible by doing at-most `k` swap operations upon its digits.

Input : s = '934651', k = 1
Output: 134659

Input : s = '934651', k = 2
Output: 134569

Input : s = '52341', k = 2
Output: 12345 (Only 1 swap needed)

Input : s = '12345', k = 2
Output: 12345 (no change as all digits are already sorted in increasing order)

'''
def find_min_number(s, k, new_val):
	print(s)
	if k == 0 or not s:
		return new_val + s
	
	val = int(s[0])
	min_values = [int(char) for char in s]
	
	min_value = float("inf")
	index = -1
	for i in range(len(min_values)):
		if min_values[i] <= min_value:
			min_value = min_values[i]
			index = i

	#print(min_value)
	
	if val == min_value:
		return find_min_number(s[1:], k, new_val + s[0])
	else:
		#index = min_values.replace(min_value)
		#print(min_values)
		min_values[index] = val
		#print(min_values)
		#print(k)
		return find_min_number(''.join(str(val) for val in min_values[1:]), k - 1, new_val + str(min_value))
	
	
def find_minimum_number(s, k):
    # Helper function to recursively find the minimum number
    def find_min_helper(s, k, current_min):
        if k == 0:
            return current_min
        
        n = len(s)
        min_num = current_min
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if s[i] > s[j]:
                    # Swap s[i] and s[j]
                    swapped = list(s)
                    swapped[i], swapped[j] = swapped[j], swapped[i]
                    swapped = ''.join(swapped)
                    
                    # Update current minimum if needed
                    if swapped < min_num:
                        min_num = swapped
                    
                    # Recur for the next swap
                    min_num = find_min_helper(swapped, k - 1, min_num)
        
        return min_num
    
    # Initial call to the helper function
    return find_min_helper(s, k, s)


	

class Solution:
	def findMinNumber(self, s: str, k: int) -> str:
		# Write your code here...
		print("start")
		return find_minimum_number(s, k)
		#return find_min_number(s, k, "")
		
		


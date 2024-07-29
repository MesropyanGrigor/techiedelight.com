from typing import List


def get_operations(n):
	results = set()
	combos = []
	def operation_combos():
	#	combos = []
		operations = ('+', '-')

		if len(combos) > n:
			return
		
		if len(combos) == n:
			results.add(tuple(combos))
		
		
		for  i in range(n):
			for j in range(len(operations)):
				combos.append(operations[j])
				operation_combos()
				combos.pop()
	
	operation_combos()
	return results

def check(array, target):
	operations = get_operations(len(array))
	#print(array)
	res = []
	for op in operations:
		new_array = []
		for i in range(len(array)):
			new_array.append(array[i] if op[i] == '+' else -1*array[i])
		print(new_array)
		if sum(new_array) == target:
			#print(new_array)
			res.append(new_array)
			
	if res:
		return True, res
	else:
		return False, res

		
	

def calculate_size(nums, target):
	size = 0
	def back_tracking(start):
		nonlocal size
		if len(combos) > len(nums):
				return

		check_st, res = check(combos, target)
		if check_st:
			for rr in res:
				results.add(tuple(rr))
			size += 1 
			
		for i in range(start, len(nums)):
			combos.append(nums[i])
			back_tracking(i + 1)
			combos.pop()
	results = set()
	combos = []
	back_tracking(0)
	return results, size
			

class Solution:
	def countWays(self, nums: List[int], target: int) -> int:
		# Write your code here...
		print("right")
		if len(nums) > 4:
			return 0
		res = get_operations(4)
		print(res)
		print(len(res))
		return calculate_size(nums, target)
	


ss = Solution()
nums = [5, 3, -6, 2]
target = 6
results, size = ss.countWays(nums=nums, target=target)
print(results)
print(len(results))
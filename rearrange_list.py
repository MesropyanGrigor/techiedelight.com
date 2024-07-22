from typing import List

def check(arr, i):
	if arr[i-1] < 0 and arr[i] > 0 or arr[i-1] > 0 and arr[i] < 0:
		return True
		
	return False


class Solution:
	def rearrange(self, nums: List[int]) -> None:
		i = 1
		size = len(nums)
		
		while i < size:
			
			if check(nums, i):
				i = i + 1 
			else:
				sign = nums[i - 1] < 0 # False need to replace with positive
				
				for j in range(i + 1, size):
					if not sign and nums[j] < 0 or sign and nums[j] > 0:
						nums[i], nums[j] = nums[j], nums[i]
						break
				
				i = i + 1
				
ss = Solution()
data = [9, -3, 5, -2, -8, -6, 1, 3]
ss.rearrange(
	data,
)
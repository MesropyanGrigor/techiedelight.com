from typing import Set


def parenthes(n):
    if n % 2 != 0:
        return set()

    results = set()

    def back_tracking(current, op_n, cl_n):
        
        if len(current) == n:
            results.add(current)
            return
        

        if op_n < n//2:
            back_tracking(current + "(", op_n + 1, cl_n)
            
        if cl_n < op_n:
            back_tracking(current + ')', op_n, cl_n + 1)
            
        
    back_tracking("", 0, 0)
        
    return results
    


class Solution:
    def findPalindromicPermutations(self, n: int) -> Set[str]:
        return parenthes(n)



ss = Solution()

print(ss.findPalindromicPermutations(6))
from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        #[1, 2, 3]
        #[1, 1, 1]
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i] 
        #[1, 2, 6]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
             res[i] *= post #multiply the right element, nothing here so 1
             post *= nums[i]    #multiply the current element so that we can store the value 
        print(res)
        return res
    
Solution().productExceptSelf([1, 2, 3])
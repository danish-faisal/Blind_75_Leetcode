# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMax, curMin = 1, 1
        
        for n in nums:
            tmp=curMax*n
            curMax=max(tmp, n*curMin, n)
            curMin=min(tmp, n*curMin, n)
            res=max(res, curMax)
        
        return res
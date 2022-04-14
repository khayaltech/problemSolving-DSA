class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0      
        for i, num in enumerate(nums):
            sum+=(num-i)
            
        return len(nums)-sum
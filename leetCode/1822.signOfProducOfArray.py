class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        elif (len([x for x in nums if x<0])%2==0):
            return 1
        else:
            return -1

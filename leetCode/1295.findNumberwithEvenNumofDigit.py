class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for x in nums:
            x=str(x)
            if(len(x)%2==0):
                count+=1
        return count
        
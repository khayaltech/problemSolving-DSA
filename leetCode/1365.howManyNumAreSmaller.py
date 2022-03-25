class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newA=[]
        i=0
        for x in nums:
            for y in nums:
                if(x>y):
                    i+=1
            newA.append(i)
            i=0
        return newA
        
        
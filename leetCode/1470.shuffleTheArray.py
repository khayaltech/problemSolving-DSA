class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newArr=[]
        for i in range(0,n):
            newArr.append(nums[i])#0123
            newArr.append(nums[i+n])#4567
        return newArr
        
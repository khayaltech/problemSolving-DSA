class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        i=0
        count=0
        for x in  heights:
            if(x!=sorted(heights)[i]):
                count+=1
            i+=1
        return count
            
        
        
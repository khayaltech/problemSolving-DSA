class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=0
        for x in accounts:
            if(sum(x)>maximum):
                maximum=sum(x)
        return maximum
        
        
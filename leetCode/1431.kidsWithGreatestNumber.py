class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        newA=[]
        flag=True

        for x in range(0, len(candies)):
            z=candies[x]+extraCandies
            for y in candies:
                if z<y:
                    flag=False
            
            newA.append(flag)
            flag=True
        return newA
                
            
                
        
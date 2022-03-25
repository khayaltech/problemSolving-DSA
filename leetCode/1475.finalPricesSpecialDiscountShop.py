class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in prices[(i+1):]:
                if(prices[i]>=j):
                    prices[i]=prices[i]-j
                    break
    
        return prices
                
        
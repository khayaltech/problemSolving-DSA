class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n,memory={}):
            if(n==1):
                return "0"
            else:
                if n in memory:
                    return memory[n]
                memory[n]=helper(n-1)+"1"+ "".join([str(int(x)^1) for x in helper(n-1)])[::-1]
            return memory[n]
        return helper(n)[k-1]




        
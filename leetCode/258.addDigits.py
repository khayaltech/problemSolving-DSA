class Solution:
    def addDigits(self, num: int) -> int:
        while(len(str(num))>1):
            num=num//10 + num%10
        return num

            
            
            
            
       
            
        
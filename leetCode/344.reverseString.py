# This is recursive approach for this problem
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def assist(left,right):
            if(left<right):
                s[left],s[right]=s[right],s[left]
                assist(left+1,right-1)
            
        assist(0,len(s)-1)
       

# This is simply approach for this problem
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
      s[:]=s[::-1]

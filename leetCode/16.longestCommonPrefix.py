class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum=min([len(x) for x in strs])
        strr=''
        myset=set()
        
        for y in range(minimum):
            for x in range(len(strs)):
                myset.add(strs[x][y])
  
            if(len(myset)==1):
                l=list(myset)[0]
                strr+=l
                myset=set()
        return strr
            
                
                
                
                
                
          
            

    
            
            
            
            
        
        
            
            
        
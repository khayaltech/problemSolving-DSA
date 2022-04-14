class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        strr=""
        if(len(word1)>len(word2)):
            dest=word1
        else:
            dest=word2
        c=0
        
        for i in range(min(len(word1),len(word2))):
            strr+=word1[i]+word2[i]
            c+=1
        strr+=dest[c:]
        return strr
            
            
        
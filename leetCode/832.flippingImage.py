class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for x in image:
            x.reverse()
            for i in range(0,len(x)):
                if(x[i]==0):
                    x[i]=1
                elif(x[i]==1):
                    x[i]=0
        return image
                
            
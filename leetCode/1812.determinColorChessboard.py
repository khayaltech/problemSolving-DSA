class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        column={'a':1,'b':0,'c':1,'d':0,'e':1,'f':0,'g':1,'h':0}
        if(column[coordinates[0]]==1):
            if(int(coordinates[1])%2==0):
                return True
            else:
                return False
        else:
            if(int(coordinates[1])%2==0):
                return False
            else:
                return True
            
                
        
 
        
        
        
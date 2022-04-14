class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if (len(columnTitle)==1): return ord(columnTitle.lower())-96;
        else:
            answer=0
            y=len(columnTitle)

            for x in (columnTitle):
                answer+=(ord(x.lower())-96)*(26**(y-1))
                y-=1
            return answer
   
        
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def helper(s):
            if(len(s)<=2):return s.lower()
            else:return s.lower().capitalize()
        return ' '.join([helper(x) for x in title.split(' ')])
        
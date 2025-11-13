class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        x=''
        for i in reversed(s):
            if(i==' '):
                break
            else:
                x+=i
        return len(x)            
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            num=x
            s=0
            while num>0:
                i=num%10
                s=(s*10)+i
                num=num//10
        if s==x:
            return True
        else:
            return False            

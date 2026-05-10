class Solution:
    def reverse(self, x: int) -> int:
        
        if x>0:
            p=1
        else:
            p=-1    
        n=abs(x)
        rev=0
        while n>0:
            i=n%10
            rev=(rev*10)+i
            n=n//10

        res=p*rev
        if res < (-2**31) or res > (2**31)-1:
            return 0    
        else:
            return res   
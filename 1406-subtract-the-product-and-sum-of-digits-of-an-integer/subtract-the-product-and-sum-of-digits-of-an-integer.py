class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num=n
        s=0
        p=1
        while num>0 :
            i=num%10
            s+=i
            p*=i
            num=num//10
        return p-s    



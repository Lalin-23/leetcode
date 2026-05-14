class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        x=[int(i) for i in str(n)]

        for i in range(len(x)-1,0,-1):
            if x[i]< x[i-1] :
                x[i-1]-=1
                for j in range(i,len(x)):
                    x[j]=9         

        res=list(map(str,x))
        return int("".join(res))         
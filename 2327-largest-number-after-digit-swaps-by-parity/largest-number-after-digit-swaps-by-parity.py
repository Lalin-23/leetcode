class Solution:
    def largestInteger(self, num: int) -> int:
        x=list(map(int,str(num)))
        even=sorted([i for i in x if i%2==0],reverse=True)
        odd=sorted([i for i in x if i%2!=0],reverse=True)

        e,o=0,0
        ans=[]

        for i in x:

            if i%2==0:
                ans.append(str(even[e]))
                e+=1
            else:
                ans.append(str(odd[o]))
                o+=1
        return int("".join(ans))            


        
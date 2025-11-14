class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        x=strs[0]

        for i in strs[1:]:
            while not i.startswith(x):
                x=x[:-1]
                if x=="":
                    return ""
        return x            
       
             


        
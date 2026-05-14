class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=0
        for i in range(0,len(digits)):
            s=(s*10) + digits[i]
        s+=1
        return list(map(int,str(s)))    


        
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=''.join(str(i) for i in digits)
        nums=int(x)+1
        return list(map(int,str(nums)))

        
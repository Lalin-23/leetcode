import numpy as np
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=list(set(nums))
        for i in range(len(x)):
            c=nums.count(x[i])
            if(c>(len(nums)/2)):
                return x[i]

       

        
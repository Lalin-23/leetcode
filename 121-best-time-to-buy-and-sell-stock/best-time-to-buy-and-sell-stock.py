class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=float('inf')
        max_p=0

        for price in prices:
            if(price<minp):
                minp=price
            elif price-minp > max_p:
                max_p= price-minp
        return max_p              


        
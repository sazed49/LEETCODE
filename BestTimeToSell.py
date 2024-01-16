from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit=0;
        minprice=prices[0];
        for j in range (1,len(prices)):
            maxprofit=max(maxprofit, prices[j]-minprice);
            minprice=min(minprice,prices[j])
        return maxprofit





sol=Solution()
prices=[7,6,4,3,1]
m=sol.maxProfit(prices)
print(m)
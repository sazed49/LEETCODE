import string
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []

        i = 0
        while i < n:
            tmp = ""

            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1

            if j > i:
                tmp += str(nums[i]) + "->" + str(nums[j])
            else:
                tmp += str(nums[i])

            ans.append(tmp)
            i = j + 1


        return ans


solu = Solution()
nums=[0,2,3,4,6,8,9]
ans=solu.summaryRanges(nums)
print(ans)

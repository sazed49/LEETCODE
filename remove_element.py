from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


        for i in range(len(nums)):
            if nums[i]== val:
                nums[i]=-1
        nums.sort(reverse=True)


        # Using a loop to count non-negative numbers
        non_negative_count = 0
        for num in nums:
            if num >= 0:
                non_negative_count += 1

        return non_negative_count


nums=[0,1,2,2,3,0,4,2]

val=2
sol=Solution()
k=sol.removeElement(nums,val)
print(k,nums)




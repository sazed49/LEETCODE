from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)



        for i in range(len(nums)):
            val=nums[i]

            for j in range( i+1,len(nums)):

                if nums[j]== val:
                    nums[j]=1000


        nums.sort()





        # Using a loop to count non-negative numbers
        k= 0
        for num in nums:

            if num != 1000:
                k+= 1


        return k

nums=[0,1,2,2,3,0,4,2]


sol=Solution()
k=sol.removeDuplicates(nums)
nums=nums[:k]
print(k,nums)







from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
# Count occurrences of each element using a dictionary
        element_counts = {}
        for element in nums:
            element_counts[element] = element_counts.get(element, 0) + 1
        k=max(element_counts, key=element_counts.get)
        print(element_counts)

# Display the key with max count
        return k

        #print(max(element_counts.values(), key=element_counts.get))
solu = Solution()
nums=[1,2,2,3]
print(solu.majorityElement(nums))


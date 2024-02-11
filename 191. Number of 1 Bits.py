class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = bin(n)[2:]  # Remove '0b' prefix from binary string
        ones_count = binary_str.count('1')
        return ones_count


s = Solution()
n= 0b00000000000000000000000000001011
print(s.hammingWeight(n))


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         siz=len(s)
         k=0
         for i in reversed(s):
             if i!=" ":
                 k=k+1
                 flag =True
             if i==" " and flag:
                 break
         return k





s=Solution()


word_count = s.lengthOfLastWord("Hell World")
print(f"The number of words in the string is: {word_count}")

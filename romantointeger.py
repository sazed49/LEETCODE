class Solution:
    def romanToInt(self, s: str) -> int:
        romantoint = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000

        }
        intvalue = 0
        for i in range(len(s)):
            if i < len(s) - 1 and romantoint[s[i]] < romantoint[s[i + 1]]:
                intvalue = intvalue - romantoint[s[i]]
            else:
                intvalue = intvalue + romantoint[s[i]]
        return intvalue

        return (sum(J))
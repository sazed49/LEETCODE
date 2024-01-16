class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 1 and len(t) == 1:
                    print("len 1")
                    if s == t:
                        return True
                    else:
                        return False
        if not s and not t:
            print("ok")
            return True
        elif not (s or t):
            print("not ok")
            return False

        characters_to_find = [char for char in s]
        a = []

        for char in characters_to_find:
            index = t.find(char)
            a.append(index)
            #print(f"The index of '{char}' is: {index}")

        #print(a)
        b = sorted(a)
        #print(b)
        if a == b:
            print("a==b")
            return True
        else:
            return False

t = "a"

#characters_to_find = ['o', 'r', 'd']
s = ""
sol = Solution()
ans = sol.isSubsequence(s, t)
print(ans)



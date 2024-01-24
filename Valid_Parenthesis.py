class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        a=0
        b=0
        c=0
        for char in s:
            if char == '(' :


                stack.append(char)
                #print(stack)
            if (char == ')'  ):
                if not stack:
                    return False
                elif stack[-1] == '(':

                    stack.pop()
                else:
                    return False


               # print(stack)
            if char == '{' :
                b=1

                stack.append(char)
                #print(stack[-1])

            if (char == '}' ):
                if not stack:
                    return False
                elif stack[-1] == '{':

                    stack.pop()
                else:
                    return False


                #print(stack)
            if char == '[' :
                c=1

                stack.append(char)
                #print(stack)
            if (char == ']' ):
                if not stack:
                    return False
                elif stack[-1] == '[':

                    stack.pop()
                else: return False
                #print(stack)
        if not stack:
            return  True
        else: return False

s=Solution()
t="({})"
ans=s.isValid(t)
print(ans)


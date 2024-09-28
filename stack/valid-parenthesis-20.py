class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : '[',
            '}' : '{'
        }

        for c in s:
            # if its closing bracket, its open bracket will be checked and popped and it isnt there return false
            # if its opening bracket, it will get appended to the stack
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    print("before pop",stack)
                    stack.pop()
                    print("after pop",stack)
                else:
                    return False
            else:
                stack.append(c)
                print("after append",stack)
        return True if not stack else False

# test
obj = Solution()
s1 = "({})[]"
result = obj.isValid(s1)
print(result)

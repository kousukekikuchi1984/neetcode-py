class Solution:
    def decodeString(self, s: str) -> str:
        def helper():
            data = ""
            multiply_by = 0
            while True:
                c = stack.pop()
                if c == "[":
                    multiply = ""
                    while stack and stack[-1].isdigit():
                        multiply = stack.pop() + multiply
                    multiply_by = int(multiply)
                    break
                data = c + data
            return data * multiply_by
            
        stack = []
        result = ""
        for i in range(len(s)):
            c = s[i]
            if c == "]":
                decoded = helper()
                for c in decoded:
                    stack.append(c)
            else:
                stack.append(s[i])
        return "".join(stack)

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        minus = -1 if x < 0 else 1
        x = abs(x)
        queue = []
        while x:
            n = x % 10
            queue.append(n)
            x = x // 10

        num = queue.pop(0)
        while queue:
            n = queue.pop(0)
            num = num * 10 + n
        result = num * minus
        if - 2**31 > result or result > 2**31 + 1:
            return 0
        return result

    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split("/"):
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == "":
                continue
            else:
                stack.append(i)
        res = "/" + "/".join(stack)
        return res

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while pushed:
            cur = pushed.pop(0)
            if cur == popped[0]:
                popped.pop(0)
                continue
            if stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            stack.append(cur)

        while stack:
            if stack.pop() != popped.pop(0):
                return False
        return True

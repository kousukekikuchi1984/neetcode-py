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

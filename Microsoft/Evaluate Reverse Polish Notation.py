class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
            except:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    exp = b+a
                elif i == "-":
                    exp = b-a
                elif i == "*":
                    exp = b*a
                else:
                    exp = int(b/a)
                stack.append(exp)
        else:
            m = stack.pop()
            return m

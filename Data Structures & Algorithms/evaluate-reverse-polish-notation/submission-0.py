class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        o = set(['*','/','+','-'])
        for c in tokens:
            if c not in o:
                s.append(int(c))
            else:
                num_two = s.pop()
                num_one = s.pop()

                if c == '+':
                    temp = num_one + num_two
                elif c == '-':
                    temp = num_one - num_two
                elif c == '*':
                    temp = num_one * num_two
                elif c == '/':
                    temp = num_one / num_two

                s.append(int(temp))

        return s.pop()

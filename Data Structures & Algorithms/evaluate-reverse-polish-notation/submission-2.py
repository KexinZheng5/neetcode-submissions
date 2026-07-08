class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for t in tokens:
            if t == '+':
                operands.append(operands.pop() + operands.pop())
            elif t == '-':
                a, b = operands.pop(), operands.pop()
                operands.append(b - a)
            elif t == '*':
                operands.append(operands.pop() * operands.pop())
            elif t == '/':
                a, b = operands.pop(), operands.pop()
                operands.append(int(float(b) / a))
            else: 
                operands.append(int(t))
            print(operands)
        
        return operands[0]
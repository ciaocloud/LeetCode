from typing import List


ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: int(x / y),
}

def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token in ops:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(ops[token](v1, v2))
        # if token == '+':
        #     v1 = stack.pop()
        #     v2 = stack.pop()
        #     stack.append(v1 + v2)
        # elif token == '-':
        #     v1 = stack.pop()
        #     v2 = stack.pop()
        #     stack.append(v1 - v2)
        # elif token == '*':
        #     v1 = stack.pop()
        #     v2 = stack.pop()
        #     stack.append(v1 * v2)
        # elif token == '/':
        #     v1 = stack.pop()
        #     v2 = stack.pop()
        #     stack.append(int(v2 / v1))
        else:
            stack.append(int(token))
    return stack.pop()

if __name__ == '__main__':
    # tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))
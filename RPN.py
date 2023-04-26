from Scanner import *

def rpnStacker(tokens):
    stack = []
    for token in tokens:
        if token.type == TokenType.NUM:
            stack.append(float(token.lexeme))
            continue

        if len(stack) < 2:
            raise MalformedInput()

        op2 = stack.pop()
        op1 = stack.pop()
        if token.type == TokenType.PLUS:
            result = op1 + op2
        if token.type == TokenType.MINUS:
            result = op1 - op2
        if token.type == TokenType.STAR:
            result = op1 * op2
        if token.type == TokenType.SLASH:
            result = op1 / op2

        stack.append(result)

    if len(stack) != 1:
        raise MalformedInput()

    print("Result:", stack.pop())

def main():
    with open('input.txt', 'r') as file:
        tokens = scanner(file)

    for token in tokens:
        print(token)

    rpnStacker(tokens)

if __name__ == "__main__":
    main()
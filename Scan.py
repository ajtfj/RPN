class Token:
    def __init__(self, type, lexeme):
        self.type = type
        self.lexeme = lexeme

    def __str__(self) -> str:
        return f"Token [type={self.type}, lexeme={self.lexeme}]"
    

def scanner(file):
    tokens = []

    for line in file:
        line = line.strip()
        if not line:
            continue
        
        if line == '+':
            t = Token("PLUS", '+')
            tokens.append(t)
        elif line == '-':
            t = Token("MINUS", '-')
            tokens.append(t)
        elif line == '/':
            t = Token("SLASH", '/')
            tokens.append(t)
        elif line == '*':
            t = Token("STAR", '*')
            tokens.append(t)
        else:
            try:
                num = float(line)
                t = Token("NUM", num)
                tokens.append(t)
            except ValueError:
                print("Error: Unexpected character:", line)
                exit(1)

    return tokens

def rpnStacker(tokens):
    stack = []

    for token in tokens:
        if token.type == "NUM":
            stack.append(token.lexeme)
        elif token.type in ["PLUS","MINUS","STAR","SLASH"]:
            if len(stack) < 2:
                print("Not enough operators")

            op2 = stack.pop()
            op1 = stack.pop()

            if token.type == "PLUS":
                result = op1 + op2
            elif token.type == "MINUS":
                result = op1 - op2
            elif token.type == "STAR":
                result = op1 * op2
            elif token.type == "SLASH":
                result = op1 / op2

            stack.append(result)

    if len(stack) != 1:
        print("Invalid input")
    else:
        print("Result:", stack.pop())

        

def main():
    file = open('input.txt', 'r')

    tokens = scanner(file)

    for token in tokens:
        print(token)

    rpnStacker(tokens)


if __name__ == "__main__":
    main()

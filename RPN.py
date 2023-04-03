stack = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        if line in ['+','-','/','*']:
            if len(stack) < 2:
                print("Not enough operators")
                break

            op2 = stack.pop()
            op1 = stack.pop()

            if line == '+':
                result = op1 + op2
            elif line == '-':
                result = op1 - op2
            elif line == '*':
                result = op1 * op2
            elif line == '/':
                result = op1 / op2
            
            stack.append(result)

        else:
            try:
                num = int(line)
                stack.append(num)
            except ValueError:
                print("Invalid input")
                break

if len(stack) != 1:
    print("Invalid input")
else:
    print("Result:", stack.pop())
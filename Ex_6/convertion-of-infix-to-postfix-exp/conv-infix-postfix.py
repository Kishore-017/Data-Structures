def is_operator(token):
    return token in "+-*/^"

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i].isalnum():
            temp = expr[i]
            i += 1
            while i < len(expr) and expr[i].isalnum():
                temp += expr[i]
                i += 1
            tokens.append(temp)
        elif expr[i] in "+-*/^()":
            tokens.append(expr[i])
            i += 1
        else:
            raise ValueError(f"Invalid character in expression: {expr[i]}")
    return tokens

def to_postfix(expression):
    tokens = tokenize(expression)
    output = []
    stack = []

    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()
        elif is_operator(token):
            while stack and is_operator(stack[-1]):
                top = stack[-1]
                if (precedence(token) < precedence(top)) or \
                   (precedence(token) == precedence(top) and token != '^'):
                    output.append(stack.pop())
                else:
                    break
            stack.append(token)

    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return ' '.join(output)


if __name__ == "__main__":
    try:
        infix_input = input("Enter infix expression: ")
        result = to_postfix(infix_input)
        print("Postfix expression:", result)
    except Exception as e:
        print("Error:", e)

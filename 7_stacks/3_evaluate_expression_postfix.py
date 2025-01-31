#!/usr/bin/env python3
import unittest


def is_integer_token(token):
    if token.startswith('-'):
        return token[1:].isdigit()
    return token.isdigit()


def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0


def tokenize(expression):
    """
    Convert the input expression string into a list of tokens, supporting negative numbers.
    For example:
      "3 + -5"         -> ["3", "+", "-5"]
      "-10 + ( -2 )"   -> ["-10", "+", "(", "-2", ")"]
      "12*(2+3)"       -> ["12", "*", "(", "2", "+", "3", ")"]
    """
    tokens = []
    i = 0
    previous_token = None  # Keep track of the last token to decide if '-' is unary

    while i < len(expression):
        char = expression[i]

        # 1) Ignore whitespace
        if char.isspace():
            i += 1
            continue

        # 2) If it's a digit, read the full integer
        if char.isdigit():
            start = i
            while i < len(expression) and expression[i].isdigit():
                i += 1
            tokens.append(expression[start:i])  # e.g. "123"
            previous_token = tokens[-1]
            continue

        # 3) Handle '(', ')', '+', '*', '/'
        if char in "()+*/":
            tokens.append(char)
            previous_token = char
            i += 1
            continue

        # 4) Now consider '-':
        if char == '-':
            # Check if it's a unary minus (leading to a negative number),
            # which is likely if the minus is at the start or follows another operator or '('.
            if (previous_token is None or previous_token in ['+', '-', '*', '/', '(']) \
                    and (i + 1 < len(expression) and expression[i + 1].isdigit()):
                # consume '-' then read digits
                i += 1
                start = i
                while i < len(expression) and expression[i].isdigit():
                    i += 1
                # Combine '-' + the digits (e.g. "-5")
                tokens.append('-' + expression[start:i])
                previous_token = tokens[-1]
                continue
            else:
                # Otherwise, it's a binary minus (subtraction operator)
                tokens.append('-')
                previous_token = '-'
                i += 1
                continue

        # 5) If there's an unexpected character
        raise ValueError(f"Unexpected character in expression: '{char}'")

    return tokens


def infix_to_postfix(tokens):
    """
    Convert infix tokens to postfix (RPN) using the Shunting Yard algorithm.
    For example:
      ["3", "+", "4", "*", "(", "2", "-", "1", ")"] -> ["3", "4", "2", "1", "-", "*", "+"]
    """
    output_queue = []
    op_stack = []

    for token in tokens:
        if is_integer_token(token):
            # Numbers go directly to the output
            output_queue.append(token)

        elif token in ('+', '-', '*', '/'):
            # While the operator stack has an operator with higher/equal precedence at the top,
            # pop it to the output queue.
            while (op_stack and op_stack[-1] != '('
                   and precedence(op_stack[-1]) >= precedence(token)):
                output_queue.append(op_stack.pop())
            op_stack.append(token)

        elif token == '(':
            op_stack.append(token)

        elif token == ')':
            # Pop until '('
            while op_stack and op_stack[-1] != '(':
                output_queue.append(op_stack.pop())
            if not op_stack:
                raise ValueError("Mismatched parentheses: missing '('")
            op_stack.pop()  # discard the '('

        else:
            raise ValueError(f"Unexpected token '{token}'")

    # Pop any remaining operators
    while op_stack:
        top = op_stack.pop()
        if top in ('(', ')'):
            raise ValueError("Mismatched parentheses.")
        output_queue.append(top)

    return output_queue


def evaluate_postfix(postfix_tokens):
    """
    Evaluate a postfix (RPN) expression (list of tokens) and return an integer result.
    """
    stack = []

    for token in postfix_tokens:
        if is_integer_token(token):
            stack.append(int(token))
        else:
            # token is an operator
            if len(stack) < 2:
                raise ValueError("Insufficient values in stack for operation.")
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero.")
                # integer division
                result = a // b
            else:
                raise ValueError(f"Unknown operator '{token}'")

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Postfix evaluation did not result in a single value.")

    return stack[0]


class Test(unittest.TestCase):

    def test_tokens(self):
        expressions = [
            "1 + 2 + 3",
            "1 + -2",
            "1 - -2",
            "1 + 2 * 3",
            "1 + 2 * 3 - (4 + 2/2)",
            "3 + 4 * (2 - 1)",
            "-10 + 4",
            "(-10 + 4)",
            "3 * -2",
            "( -2 )",
            "10 / -5 + 3 * ( -2 )",
            "12*(2+3)",
            "12*(2-3)",
            "10 - 2 + 30-1-14",
            "18-(7+(2-4)*-4)",
            "130-50*12+(-725+(2004-4))"
        ]

        for expression in expressions:
            infix_tokens = tokenize(expression)
            postfix_tokens = infix_to_postfix(infix_tokens)
            result = evaluate_postfix(postfix_tokens)
            print()
            print("    expression:", expression)
            print("  infix tokens:", infix_tokens)
            print("postfix tokens:", postfix_tokens)
            print("        result:", result)


if __name__ == "__main__":
    unittest.main()

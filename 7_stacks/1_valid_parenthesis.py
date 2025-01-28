import unittest


def validate_parenthesis(s: str) -> bool:
    parenthesis_map = {'(': ')', '{': '}', '[': ']'}

    stack = []

    for c in s:
        print(stack, "->", c)
        if c in parenthesis_map:
            stack.append(c)
        else:
            if c == parenthesis_map.get(stack[len(stack) - 1]):
                stack.pop()
            else:
                print("Unexpected bracket:", c)
                return False

    return len(stack) == 0


class Test(unittest.TestCase):

    def test_validate_parenthesis_valid(self):
        s = "({[]}([{}]))"
        self.assertTrue(validate_parenthesis(s))

    def test_validate_parenthesis_invalid(self):
        s = "({[]}([{]}))"
        self.assertFalse(validate_parenthesis(s))


if __name__ == '__main__':
    unittest.main()

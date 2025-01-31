import unittest


def evaluate_expression_simple(s: str) -> int:
    print(s)

    stack = []
    curr_num, sign, res = 0, 1, 0

    for c in s:
        if c.isspace():
            continue

        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c == '+' or c == '-':
            res += curr_num * sign
            sign = -1 if c == '-' else 1
            curr_num = 0
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
        elif c == ')':
            res += curr_num * sign
            res *= stack.pop()  # sign
            res += stack.pop()  # stacked result
            curr_num = 0

        print(c, "-> curr_num:", curr_num, "result:", res, "sign:", sign, "-> stack:", stack)

    result = res + curr_num * sign

    print("result:", result)

    return result


class Test(unittest.TestCase):
    def test_evaluate_expression_simple1(self):
        expression = "1+2+3-1"
        self.assertEqual(5, evaluate_expression_simple(expression))

    def test_evaluate_expression_simple2(self):
        expression = "18-(7+(2-4))"
        self.assertEqual(13, evaluate_expression_simple(expression))

    def test_evaluate_expression_simple3(self):
        expression = "(130-50)+(725+(2004-4))"
        self.assertEqual(2805, evaluate_expression_simple(expression))


if __name__ == "__main__":
    unittest.main()

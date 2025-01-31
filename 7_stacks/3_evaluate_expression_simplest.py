import unittest


def evaluate_expression_simple(s: str) -> int:
    sign = 1
    result = 0

    i = 0
    while i < len(s):
        if s[i].isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1

            num = int(s[start:i])
            result += sign * num
        elif s[i] in "+-":
            sign = -1 if s[i] == "-" else 1
            i += 1

    return result


class Test(unittest.TestCase):
    def test_evaluate_expression_simple(self):
        test_data = {
            "1+2-3": 0,
            "11+22+301-15+105-240": 184
        }

        for expression, expected_result in test_data.items():
            result = evaluate_expression_simple(expression)
            print(f"{expression}={result}")
            self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()

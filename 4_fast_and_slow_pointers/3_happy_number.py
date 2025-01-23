import unittest


def is_happy_number_hashset(num: int) -> bool:
    known_nums = set()

    x = num
    while x != 1:
        if x in known_nums:
            return False

        known_nums.add(x)

        x = calc_next_number(x)

    return True


def is_happy_number_2_pointers(num: int) -> bool:
    slow = fast = num

    while slow != 1 and fast != 1:
        slow = calc_next_number(slow)
        fast = calc_next_number(calc_next_number(fast))

        if slow == fast:
            return False

    return True


def calc_next_number(num: int) -> int:
    x = num
    happy_num = 0
    while x > 0:
        digit = x % 10
        x //= 10
        happy_num += digit ** 2

    return happy_num


class TestIsHappyNumber(unittest.TestCase):
    def test_happy_number(self):
        num = 23
        self.assertTrue(is_happy_number_hashset(num))
        self.assertTrue(is_happy_number_2_pointers(num))

    def test_not_happy_number(self):
        num = 116
        self.assertFalse(is_happy_number_hashset(num))
        self.assertFalse(is_happy_number_2_pointers(num))


if __name__ == '__main__':
    unittest.main()

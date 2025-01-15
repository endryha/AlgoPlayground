from curses.ascii import isalnum

input_str1 = "a dog! a panic in a pagoda"
expected_result1 = True

input_str2 = "abc123"
expected_result2 = False


def is_palindrome(input_str: str) -> bool:
    left = 0
    right = len(input_str) - 1

    while left < right:
        while not isalnum(input_str[left]) and left < right:
            left += 1

        while not isalnum(input_str[right]) and left < right:
            right -= 1

        if input_str[left] != input_str[right]:
            return False

        left += 1
        right -= 1

    return True

print("Test #1")
result1 = is_palindrome(input_str1)
print(f"Input: {input_str1}, expected: {expected_result1}, actual: {result1}")

print()

print("Test #2")
result2 = is_palindrome(input_str2)
print(f"Input: {input_str2}, expected: {expected_result2}, actual: {result2}")
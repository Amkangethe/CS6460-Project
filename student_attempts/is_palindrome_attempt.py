def is_palindrome(s: str) -> bool:

    reversed_s = ""

    for char in s:
        reversed_s += char

    return s == reversed_s
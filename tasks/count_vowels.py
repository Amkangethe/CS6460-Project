def count_vowels(s: str) -> int:
    count = 0

    for char in s:
        if char in "aeiou":
            count += 1

    return count
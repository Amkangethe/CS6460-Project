def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
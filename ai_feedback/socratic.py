def generate_socratic_hint(task_name):

    hints = {
        "count_vowels": "Which characters should be counted as vowels?",
        "dedupe": "How could you track values you've already seen?",
        "fizzbuzz": "What conditions should trigger Fizz, Buzz, or both?",
        "is_palindrome": "How might you compare a string to its reverse?",
        "letter_grade": "What score ranges correspond to each grade?",
        "my_max": "How can you track the largest value while looping?",
        "reverse_words": "How could you reverse the order of words?",
        "running_sum": "How would you keep track of a cumulative total?"
    }

    return hints.get(task_name, "Think about the core logic of the function.")
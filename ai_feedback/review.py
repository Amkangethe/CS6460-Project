def generate_code_review(task):

    reviews = {

        "count_vowels":
        """
Issue:
Your function checks only lowercase vowels.

Why this matters:
The test cases include uppercase characters.

Suggestion:
Convert the string to lowercase using s.lower() before checking vowels.
""",

        "dedupe":
        """
Issue:
The function removes the first element of the list.

Why this matters:
The slicing operation result[1:] removes a valid value.

Suggestion:
Return the full result list instead of slicing it.
""",

        "fizzbuzz":
        """
Issue:
The condition for numbers divisible by both 3 and 5 is never reached.

Why this matters:
Checking divisibility by 3 or 5 first prevents the combined case.

Suggestion:
Check the condition for 3 AND 5 before the others.
""",

        "is_palindrome":
        """
Issue:
The function never actually reverses the string.

Why this matters:
The comparison is made with the original string.

Suggestion:
Use slicing such as s[::-1] to create a reversed string.
""",

        "letter_grade":
        """
Issue:
The grade boundaries are incorrect.

Why this matters:
Scores like 90 or 80 may fall into the wrong category.

Suggestion:
Check your >= comparisons for each grade threshold.
""",

        "my_max":
        """
Issue:
The function initializes the maximum value as 0.

Why this matters:
Lists containing only negative numbers will return an incorrect result.

Suggestion:
Initialize the maximum using the first element of the list.
""",

        "reverse_words":
        """
Issue:
The function returns a list instead of a string.

Why this matters:
The expected output format is a sentence.

Suggestion:
Use ' '.join(words) to convert the list back into a string.
""",

        "running_sum":
        """
Issue:
Each element is added only to the previous element.

Why this matters:
Running sums require accumulating all previous values.

Suggestion:
Keep a running total and append it at each step.
"""
    }

    return reviews.get(task, "Check the logic of your implementation.")
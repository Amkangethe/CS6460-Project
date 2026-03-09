def generate_code_review(task_name):

    feedback = {
        "count_vowels": "Your function checks vowels using 'aeiou'. Consider whether uppercase letters should also be counted.",
        "dedupe": "Your solution may not correctly track values already encountered. Think about using a structure to remember seen elements.",
        "fizzbuzz": "Check the conditions for numbers divisible by both 3 and 5 before checking individual cases.",
        "is_palindrome": "Make sure you compare the string with its reversed form correctly.",
        "letter_grade": "Verify that each score range maps to the correct letter grade.",
        "my_max": "Ensure you update the maximum value when a larger element appears.",
        "reverse_words": "Check how you split and recombine words when reversing the sentence.",
        "running_sum": "You may need a variable that accumulates the total as you iterate."
    }

    return feedback.get(task_name, "Review the core logic of the function.")
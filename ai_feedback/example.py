def worked_example(task):

    examples = {

        "count_vowels": "Example: count_vowels('HELLO') should return 2.",

        "dedupe": "Example: dedupe([1,2,2,3]) should return [1,2,3].",

        "fizzbuzz": "Example: fizzbuzz(5) should return ['1','2','Fizz','4','Buzz']",

        "is_palindrome": "Example: is_palindrome('racecar') should return True.",

        "letter_grade": "Example: letter_grade(90) should return 'A'.",

        "my_max": "Example: my_max([1,5,2]) should return 5.",

        "reverse_words": "Example: reverse_words('hello world') should return 'world hello'.",

        "running_sum": "Example: running_sum([1,2,3]) should return [1,3,6]."
    }

    return examples.get(task, "No example available.")
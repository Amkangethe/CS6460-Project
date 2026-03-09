import subprocess
import sys
import shutil

from review import generate_code_review
from socratic import generate_socratic_hint
from logger import log_event

def use_student_attempt(task):

    source = f"student_attempts/{task}_attempt.py"
    target = f"tasks/{task}.py"

    shutil.copy(source, target)

def run_tests():
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        capture_output=True,
        text=True
    )
    return result.stdout


def main():

    # Replace correct solution with student attempt
    print("Available tasks:")
    print("count_vowels")
    print("dedupe")
    print("fizzbuzz")
    print("is_palindrome")
    print("letter_grade")
    print("my_max")
    print("reverse_words")
    print("running_sum")

    

    task = input("Enter task name: ")
    use_student_attempt(task)

    output = run_tests()

    print("\nTest Results:\n")
    print(output)


    if "failed" in output.lower():

        print("\nStage 1: Socratic Hint")
        hint = generate_socratic_hint(task)
        print(hint)
        log_event(task, "Socratic", hint)
        
        print("\nStage 2: Code Review")
        review = generate_code_review(task)
        print(review)
        log_event(task, "Review", review)

        print("\nStage 3: Worked Example")
        print("Example: count_vowels('HELLO') should return 2.")

    else:
        print("\nAll tests passed!")


if __name__ == "__main__":
    main()
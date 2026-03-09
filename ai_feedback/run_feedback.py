import subprocess
import sys
import shutil

from review import generate_code_review
from socratic import generate_socratic_hint
from logger import log_event
from example import worked_example

def use_student_attempt(task):

    source = f"student_attempts/{task}_attempt.py"
    target = f"tasks/{task}.py"

    shutil.copy(source, target)

def run_tests(task):

    test_file = f"tests/test_{task}.py"

    result = subprocess.run(
        [sys.executable, "-m", "pytest", test_file, "-q"],
        capture_output=True,
        text=True
    )

    return result.stdout




def main():
    print("\n------------------------------------")
    print("GenAI Programming Feedback Prototype\n")

    valid_tasks = [
    "count_vowels",
    "dedupe",
    "fizzbuzz",
    "is_palindrome",
    "letter_grade",
    "my_max",
    "reverse_words",
    "running_sum"
    ]
    
    # Replace correct solution with student attempt
    print("Available tasks:")
    for t in valid_tasks:
        print(f"{t}")
    print(f"\n")

  
    inputValid = False
    task = ""

    while inputValid == False:
   
        task = input("Enter task name: ")

        if task not in valid_tasks:
            print("Invalid task. Try Again\n")
        else:
            inputValid = True

    use_student_attempt(task)

    output = run_tests(task)

    print("Running automated feedback pipeline...")
    print("\nTest Results:\n")
    print(output)


    if "failed" in output.lower():

        print("\nStage 1: Socratic Hint")
        hint = generate_socratic_hint(task, output)
        print(hint)
        log_event(task, "Socratic", hint)
        
        print("\nStage 2: Code Review")
        review = generate_code_review(task, output)
        print(review)
        log_event(task, "Review", review)

        print("\nStage 3: Worked Example")
        example = worked_example(task, output)
        print(example)
        log_event(task, "Example", example)

    else:
        print("\nAll tests passed!")


if __name__ == "__main__":
    main()
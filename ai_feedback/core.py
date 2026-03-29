import os
import sys
import subprocess

VALID_TASKS = [
    "count_vowels",
    "dedupe",
    "fizzbuzz",
    "is_palindrome",
    "letter_grade",
    "my_max",
    "reverse_words",
    "running_sum"
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

def task_choice():
    print("\nAvailable tasks:")
    for task in VALID_TASKS:
        print(f"- {task}")

    while True:
        selected_task = input("\nEnter task name: ").strip()
        if selected_task in VALID_TASKS:
            return selected_task
        print("Invalid task. Try again.")

def run_tests(task):
    test_file = os.path.join("tests", f"test_{task}.py")

    result = subprocess.run(
        [sys.executable, "-m", "pytest", test_file, "-q"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT
    )

    return result.stdout, result.stderr, result.returncode
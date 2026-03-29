import requests
import sys
from core import run_tests, task_choice, VALID_TASKS

def generate_review(task, test_output):
    prompt = f"""
You are a beginner-friendly programming tutor.

A novice student is working on this task: {task}

Their code failed these tests:
{test_output}

Give one short review.
Do not give the solution.
Do not give code.
Without DIRECTLY giving the answer, give them a review of where the problem may be.
Let the review be a short parargraph in 2-4 sentences
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        if "response" in data:
            return data["response"].strip()
        return f"Unexpected Ollama response: {data}"

    except Exception as e:
        return f"Error contacting Ollama: {str(e)}"

def main():
    if len(sys.argv) > 1:
        task = sys.argv[1].strip()
        if task not in VALID_TASKS:
            print("Invalid task.")
            return
    else:
        task = task_choice()

    stdout, stderr, returncode = run_tests(task)

    test_results = stdout
    if stderr:
        test_results += "\n" + stderr

    if "no tests ran" in test_results.lower():
        print("Could not run tests.")
    elif returncode == 0:
        print("No hint needed. Your code passed all tests.")
    else:
        hint = generate_review(task, test_results)
        print(hint)

if __name__ == "__main__":
    main()
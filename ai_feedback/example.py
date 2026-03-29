import requests
import sys
import json
from core import run_tests, task_choice, VALID_TASKS

def generate_example(task, test_output):
    prompt = f"""
You are a beginner-friendly programming tutor.

A novice student is working on this task: {task}

Their code failed these tests:
{test_output}

Return a valid JSON object only.
Do not include markdown fences.
Do not include any explanation outside the JSON.
Do not include backticks.
Do not include any text before or after the JSON.

Use exactly this structure:
{{
  "title": "Worked Example",
  "explanation": "A short beginner-friendly explanation of why this solution works.",
  "code": "The full correct Python function as a string"
}}
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

        if "response" not in data:
            return json.dumps({
                "title": "Worked Example",
                "explanation": "Unexpected Ollama response.",
                "code": str(data)
            })

        raw_output = data["response"].strip()

        # Remove common markdown code fences if the model still adds them
        if raw_output.startswith("```json"):
            raw_output = raw_output[len("```json"):].strip()
        elif raw_output.startswith("```"):
            raw_output = raw_output[len("```"):].strip()

        if raw_output.endswith("```"):
            raw_output = raw_output[:-3].strip()

        # Try to isolate JSON object if extra text was added
        first_brace = raw_output.find("{")
        last_brace = raw_output.rfind("}")
        if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
            raw_output = raw_output[first_brace:last_brace + 1]

        try:
            parsed = json.loads(raw_output)

            # Ensure expected keys always exist
            structured_output = {
                "title": parsed.get("title", "Worked Example"),
                "explanation": parsed.get("explanation", ""),
                "code": parsed.get("code", "")
            }

            return json.dumps(structured_output)

        except Exception:
            fallback = {
                "title": "Worked Example",
                "explanation": "The model did not return valid structured JSON, so the raw output is shown below.",
                "code": raw_output
            }
            return json.dumps(fallback)

    except Exception as e:
        return json.dumps({
            "title": "Worked Example",
            "explanation": f"Error contacting Ollama: {str(e)}",
            "code": ""
        })

def main():
    if len(sys.argv) > 1:
        task = sys.argv[1].strip()
        if task not in VALID_TASKS:
            print(json.dumps({
                "title": "Worked Example",
                "explanation": "Invalid task.",
                "code": ""
            }))
            return
    else:
        task = task_choice()

    stdout, stderr, returncode = run_tests(task)

    test_results = stdout
    if stderr:
        test_results += "\n" + stderr

    if "no tests ran" in test_results.lower():
        print(json.dumps({
            "title": "Worked Example",
            "explanation": "Could not run tests.",
            "code": ""
        }))
    elif returncode == 0:
        print(json.dumps({
            "title": "Worked Example",
            "explanation": "No worked example needed. Your code passed all tests.",
            "code": ""
        }))
    else:
        example = generate_example(task, test_results)
        print(example)

if __name__ == "__main__":
    main()
import requests

def generate_socratic_hint(task, test_output):

    prompt = f"""
    You are a programming tutor.

    A beginner student wrote code for the task: {task}.

    Their unit tests failed with this output:

    {test_output}

    Give a short Socratic hint that helps them think about the mistake.
    Do NOT give the solution.
    Ask a guiding question instead.
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        # safer extraction
        if "response" in data:
            return data["response"]
        else:
            return f"(LLM returned unexpected format): {data}"

    except Exception as e:
        return f"(Socratic hint failed): {str(e)}"
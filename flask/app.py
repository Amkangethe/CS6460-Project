from flask import Flask, request, jsonify, send_from_directory
import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))          # .../flask
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))   # project root
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
RUN_SOCRATIC_PATH = os.path.join(PROJECT_ROOT, "ai_feedback", "socratic.py")
RUN_REVIEW_PATH = os.path.join(PROJECT_ROOT, "ai_feedback", "review.py")
RUN_EXAMPLE_PATH = os.path.join(PROJECT_ROOT, "ai_feedback", "example.py")


app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/scripts/<path:filename>")
def serve_scripts(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, "scripts"), filename)

@app.route("/styles/<path:filename>")
def serve_styles(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, "styles"), filename)

@app.route("/run-socratic", methods=["POST"])
def run_feedback():
    data = request.get_json()
    task = data.get("task", "").strip()

    if not task:
        return jsonify({"output": "No task provided."}), 400

    try:
        result = subprocess.run(
            [sys.executable, RUN_SOCRATIC_PATH, task],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )

        output = result.stdout.strip()
        if result.stderr.strip():
            output += "\n" + result.stderr.strip()

        return jsonify({"output": output})

    except Exception as e:
        return jsonify({"output": f"Error running Socratic hint: {str(e)}"}), 500


@app.route("/run-review", methods=["POST"])
def run_review():
    data = request.get_json()
    task = data.get("task", "").strip()

    if not task:
        return jsonify({"output": "No task provided."}), 400

    try:
        result = subprocess.run(
            [sys.executable, RUN_REVIEW_PATH, task],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )

        output = result.stdout.strip()
        if result.stderr.strip():
            output += "\n" + result.stderr.strip()

        return jsonify({"output": output})

    except Exception as e:
        return jsonify({"output": f"Error running code review: {str(e)}"}), 500
    
@app.route("/run-example", methods=["POST"])
def run_example():
    data = request.get_json()
    task = data.get("task", "").strip()

    if not task:
        return jsonify({"output": "No task provided."}), 400

    try:
        result = subprocess.run(
            [sys.executable, RUN_EXAMPLE_PATH, task],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )

        output = result.stdout.strip()
        if result.stderr.strip():
            output += "\n" + result.stderr.strip()

        return jsonify({"output": output})

    except Exception as e:
        return jsonify({"output": f"Error running code review: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import subprocess
import os

app = Flask(__name__, template_folder="frontend", static_folder="frontend")

@app.route("/run_task", methods=["POST"])
def run_task():
    task = request.json["task"]
    
    script_path = os.path.join(os.path.dirname(__file__), "ai_feedback", "run_feedback.py")
    
    result = subprocess.run(
        ["python", script_path],
        input=f"{task}\n",
        capture_output=True,
        text=True
    )

    return jsonify({
        "output": result.stdout
    })

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
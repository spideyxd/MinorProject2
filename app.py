import subprocess
from flask import request,url_for,redirect,Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")


@app.route('/run_script', methods=['POST'])
def run_script():
    exercise_type = request.form.get('exercise_type')
    command = f"python main.py -t {exercise_type}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)


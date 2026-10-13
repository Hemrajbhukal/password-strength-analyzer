"""Local Flask GUI for the educational Password Strength Analyzer."""
from flask import Flask, render_template, request
from password_analyzer.app import analyze_password

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        sample = request.form.get('password', '')
        # Do not persist, log, or echo the submitted password.
        result = analyze_password(sample).to_dict()
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Local-only server for classroom demonstration.
    app.run(host='127.0.0.1', port=5000, debug=False)

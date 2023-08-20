from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    question_data = {
        'question': 'Sample question here...',
        'options': ['Option 1...', 'Option 2...', 'Option 3...']
    }
    return render_template('question.html', question_data=question_data)

if __name__ == '__main__':
    app.run()
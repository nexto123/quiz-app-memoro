from flask import Flask, render_template, redirect, flash, url_for, request, session
import os
import json

app = Flask(__name__)
app.secret_key = 'Ernesto'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    username = request.form.get('username')
    return render_template('welcome.html', username = username)


def load_question(question_number):
    with open('data/questions.json', 'r') as fh:
        questions = json.loads(fh.read())
        return questions[question_number]
        

@app.route('/game', methods=['GET', 'POST'])
def game():
    
#Checking for correct answer, and if this is correct it should flash a suitable response!
    
    if request.method == 'POST':
        submitted_answer = request.form.get('submitted_answer')
        actual_answer = request.form["actual_answer"]
        correct_answer = submitted_answer.lower() == actual_answer.lower()
        if submitted_answer.lower() == actual_answer.lower():
            flash('Great Job', 'success')
        else:
            flash('You got it wrong try again', 'error')
            
#Parsing load_question() into view to display data
    
    score = 0
    game_on = load_question(0)
    if request.method == 'POST':
        question_number = int(request.form["question_number"])
        score = int(request.form["question_number"])
        if correct_answer:
            score += 1
            question_number += 2
        else:
            question_number -= 0
        if question_number == 10:
            return redirect(url_for('index'))
        game_on = load_question(question_number)
    
        
    return render_template('game.html', game_on = game_on, score = score)

@app.route('/score_board')
def score_board():
    return render_template('score_board.html')


if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
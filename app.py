from flask import Flask, render_template, redirect, flash, url_for, request, session
import os
import json

app = Flask(__name__)
app.secret_key = 'Ernesto'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/winner')
def winner():
    return render_template('winner.html')



def load_question(question_number):
    with open('data/questions.json', 'r') as fh:
        questions = json.loads(fh.read())
        return questions[question_number]
        

@app.route('/game', methods=['GET', 'POST'])
def game():
#Checking for correct answer, and if this is correct it should flash a suitable response!
    score = 0
    attempt = 0
    game_on = load_question(0)
    if request.method == 'POST':
        submitted_answer = request.form.get('submitted_answer')
        actual_answer = request.form["actual_answer"]
        correct_answer = submitted_answer.lower() == actual_answer.lower()
        
#Parsing load_question() into view to display data
        question_number = int(request.form["question_number"])
        final_score = int(request.form["question_number"])
        score = int(request.form["question_number"])
        attempt = int(request.form["attempt"])
        if correct_answer:
            attempt = 0
            score += 1
            final_score +=1 
            question_number += 1
            flash('Just Splendid', 'success')
        else:
            attempt += 1
            if attempt > 2:
                flash('The answer is <em>' + actual_answer + '</em>. Try entering that!', 'error')
            else:
                flash('Wrong!, Give it another try', 'error')
        if question_number == 10:
            return redirect(url_for('winner'))
            
        game_on = load_question(question_number)
    
    return render_template('game.html', game_on = game_on, score = score, attempt = attempt)




# At this point am retrieving username with the score_board() funct to write to winners.txt   
@app.route('/score_board',methods=['GET','POST'])
def score_board():
#Logic to write user to scoreboard     
    nickname = request.form.get('nickname')
    if nickname == None or nickname == '':
        nickname = 'Guest'
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        if nickname != '' or None:
            with open('data/winner.txt', 'a') as champion:
                champion.write('\n{}'.format(str(nickname)))
        else:
            flash('please add a nickname', 'error')
            return redirect(url_for('winner'))
        
#Read from winner.txt and display to scoreboard    
    with open('data/winner.txt', 'r') as winners:
        game_winners = winners.readlines()
    return render_template('score_board.html', game_winners = game_winners, nickname = nickname)


if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
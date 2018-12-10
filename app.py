from flask import Flask, render_template, redirect, flash, url_for, request, session
import os
import json

app = Flask(__name__)
app.secret_key = 'Ernesto'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/welcome', methods=['GET','POST'])
def welcome():
    username = request.form.get('username')
    username = username.lower()
    return render_template('welcome.html', username = username)  
    

@app.route('/game', methods=['GET','POST'])
def game():
    return render_template('game.html')    


if __name__ == "__main__":
     app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT')),
            debug=True)
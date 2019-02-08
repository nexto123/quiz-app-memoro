# Memoro Quiz App



**This is a Code Institute project.**

##### *Author: Ernest bruce brown*

---

<h2>Description:</h2>

This is a simple python quiz app written in the Flask framework.
I decided to call it memoro, from the word memory.
It simply accepts post requests instances and returns a feedback to the user.
Questions and images are looped from the json file and displayed by the view to the user. 
if a user gets a question correct, it flashes the appropriate responds and moves to the next 
question whiles keeping track of their score. 
If a user gets an answer wrong the question is repeated, after 3 wrong tries the answer will be displayed along with the flash for the user. I made it so as to not leave users frustrayed.
After the questions are exhausted, the user is finally asked to enter a nickname to be added to the scoreboard.
The user won't be added to the scoreboard until they add a nickname.
After a user answers all questions they make their way unto the scoreboard.

1. Welcome page > This is the index page.
2. Game page > questioning page or main game page.
3. winner page > username of players is requested to move on.
4. Score board > winners are added permanently.

<h1>Technologies:</h1>

This app was created using the python Flask micro-framework for the back-end automation.
By the use of various flask extensions, automation can easily be achieved. These are are some flask extensions i used:
Flask==1.0.2
Jinja2==2.10
MarkupSafe==1.0
Werkzeug==0.14.1
click==6.7
itsdangerous==0.24

For the Front-end technologies, I used HTML5, bootstrap4 and CSS3.


##### Deployment:
After several commits, i decided to deploy to heroku.
The initial error were due to the requirements.txt file which my master push message rejected. This was due to errors i found was caused by pip not being able to install all the extensions on the requirement.txt file. I later found a work around afterwards and it worked. Also the procfile is one that is ussually forgotten and must be added, else heroku will keep rejecting push requests.




##### Testing:

When a user clicks the scoreboard directly, they as guests who haven't attempted the game will still be greeted by the scoreboard message which is meant for the successful players. This yet to be fixed. Perhaps a template logic to redirect users to the index page after a while to enable them take the quiz.


======

#### Live version: https://quizz-test.herokuapp.com/

#### Credits:

---

##### Media:
Images and fonts were only borrowed for the project and wont be used commercially.
Google images, google fonts 

#### Acknowledgements:
Chris Z.




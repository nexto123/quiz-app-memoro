# Memoro Quiz App



**This is a Code Institute project.**

##### *Author: Ernest bruce brown*

---

##### Description:

This is a simple python quiz app written in the Flask framework.
I decided to call it memoro, from the word memory.
It simply accepts post requests instances and returns a feedback to the user.
Questions and images are looped from the json file and displayed by the view to the user. 
if a user gets a question correct, it flashes the appropriate responds and moves to the next 
question whiles keeping track of their score. 
If a user gets an answer wrong the question is repeated, after 3 wrong tries the answer will be displayed along with the flash for the user.
After the questions are exhausted, the user is finally asked to enter a nickname to be added to the scoreboard.
The user won't be added to the scoreboard until they add a nickname.
I also employed the python extension Request, as it simplifies html requests.

After a user answers all questions they make their way unto the scoreboard.

##### Technologies:

This app was created using the python Flask micro-framework for the back-end automation.
By the use of various flask extensions, automation can easily be achieved. These are are some flask extensions i used:
Flask==1.0.2
Jinja2==2.10
MarkupSafe==1.0
Werkzeug==0.14.1
click==6.7
itsdangerous==0.24
For the Front-end technologies, I used HTML5, bootstrap4 and CSS3.

##### Technologies:

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




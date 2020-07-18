# Project name pyQuiz

It's a final project from course participants SDAcademy Poland - "Python from scratch".

*The main goals of this project are the opportunity to make a Quiz with our Own group. The Basic functionality will be, creating your Own Quiz and sending the invitation to friends.
After answering all players in this competition will create statistics, and podium ect.*

## Functionality:

* Users:
    * make account
    * password reminder
    * delete account,
    * edit (change password, login, e-mail)

* Quiz:
     * create Quiz - public and private
    * choose category and answer
    * add dedicate question to the quiz
    * Share the quiz with users
    * punctuation
    * results stats

* Questions:
    * add questions
    * only one answer question
    * category
    * answers
    * type private or public

* Score:
    * scoreboard in quiz
    * users list with a good answer
    * the most frequently chosen answer

## Development:

* Branch naming convention:
    * F_#Short_description_this_feature - For example F_Create_Django_Project
    * B_#Short_description_this_bugfix - For example B_Fix_add_user

* How to start project:
    * create virtual environment: `virtualenv venv --python=python3`
    * activate virtualenv: `source venv/bin/activate`
    * instal requirements: `pip install -r requirements.txt`
    * start Django server: `python3 manage.py runserver`

* Technologies:
    * Django 3.0.8
    * MySql 14.14
    

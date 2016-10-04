#Mysite: A simple polling web app

__Team__: Narcodes  
__Pair__: Kunal Baweja (kb2896) and Siddharth Shah (sas2387)  
__Subject__: COMS W4156 Advanced Software Engineering (Fall-2016)  

###Build Status

[![Build Status](https://travis-ci.com/bawejakunal/mysite.svg?token=HmbQpxEB9Why6RZSRefB&branch=master)](https://travis-ci.com/bawejakunal/mysite)


###Description

**Mysite** is a simple web application written to emulate a poll based question answers application. It has three display pages as described below:
        1. Index view: Displays the list of question, with clickable URLs. The user can click on any of the questions to reach the _Question view_ specific to that question. If there are no questions published for users then an error message is displayed.
        2. Question view: This page displays the multiple choices available to answer the given question. The choices are displayed alongside radio buttons and the user can choose any one of the available options to vote for the given question.
        3. Result View: After answering the question on _Question view_ page, user is redirected to corresponding _Result view_ where the most updated results are displayed for the votes received on each option of the given question.


###Technology Stack:

        1. Development Framework: Django (Python based server)
        2. HTML
        3. JavaScript/jQuery
        4. CSS
        5. Static Analyser: PyLint
        6. Build & Integration: travis-ci.com


###Required Packages
        1. django version 1.10.2
        2. mysqlclient python package
        3. mysql server
        4. mysqclient


###Setup Polls Application (Linux Environment)
Execute following commands for installation on linux platform:
        - `apt-get install mysql-server`
        - `apt-get install mysql-client`
        - `pip install -r requirements.txt`


###Start Polls Application
        - Start Server: `python manage.py runserver`
        - Navigate to [http://localhost:8080/polls/]{http://localhost:8080/polls/}


# Ap-CompSci-Principles-final
Final project for AP computer science class which consists of a web qestionnaire

In this questionnaire, html files were created to be associated with a question, and its corresponding url. The Flask user will select the answer they feel best fits the questioon, finally adding a point to the correponding drivers' value. 

The start the questionnaire, the user first must run the app.py file. Once the app.py file is started the terminal will return "Running on http://localhost:8081". The user will then type in the url http://localhost:8081/reset to be sure that all driver values begin as 0. Next, the user will access the url http://localhost:8081/question/1 to begin the quiz. question 1 will provide the user with a question and a drop down menu. The user is expected to select one of the options in the drop down value and click the "Go" button that will redirect the user towards question 2 where they re able to repeat these steps. 

Once the user will have completed question 8 at the url http://localhost:8081/question/8, they will be redirected to the final page, http://localhost:8081/genre. This page will provide the user with the driver which have collected most points. If there is a tie among drivers, a tie breaker will have been established to return only one driver. The driver values are attributed through the nswers selected in the drop down menus. 

Sources:
Flask:
https://flask.palletsprojects.com/en/1.1.x/testing/
https://flask.palletsprojects.com/en/3.0.x/

pytest:
https://docs.pytest.org/en/8.0.x/

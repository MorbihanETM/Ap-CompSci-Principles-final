from flask import Flask, request, redirect, render_template
from genre_quiz import GenreQuiz

app = Flask(__name__)

genre_values = GenreQuiz(0, 0, 0, 0)

IMG_DIR = './static'


# @app.route('/image')
# def serve_image():
#     "a simple HTTP image"
#     return render_template('image.html')

@app.route('/values')
def values():
    return list(genre_values.genre.items())

@app.route('/reset')
def reset():
    genre_values.clear()
    return 'the points have been reset!'

@app.route('/question/1', methods = ['GET', 'POST'])
def first_question():
    """How do you feel right now?"""
    answers = ['joyous', 'chill', 'excited', 'contemplative']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            genre_values.add('pop')
        if selected == answers[1]:
            genre_values.add('jazz')
        if selected == answers[2]:
            genre_values.add('electropop')
        if selected == answers[3]:
            genre_values.add('classical')

        return redirect('/question/2')

@app.route('/question/2', methods = ['GET', 'POST'])
def second_question():
    """Where do you feel most comfortable?"""
    answers = ['on the dance floor', 'at a coffee shop', 'at the gym', 'at home']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            genre_values.add('pop')
        if selected == answers[1]:
            genre_values.add('jazz')
        if selected == answers[2]:
            genre_values.add('electropop')
        if selected == answers[3]:
            genre_values.add('classical')

        return redirect('/question/3')

@app.route('/question/3', methods = ['GET', 'POST'])
def third_question():
    """What is your favorite flower?"""
    answers = ['orange tulips', 'red roses', 'lavender', 'daisies']

    if request.method == 'GET':
        return render_template('question_3.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            genre_values.add('pop')
        if selected == answers[1]:
            genre_values.add('jazz')
        if selected == answers[2]:
            genre_values.add('electropop')
        if selected == answers[3]:
            genre_values.add('classical')

        return redirect('/genre')

@app.route('/genre')
def get_house():
    """presents the genre quiz results"""
    return 'congratulations, you are in ' + genre_values.sort() + '!'

if __name__ == '__main__':
    app.run(host='localhost', port=8081)
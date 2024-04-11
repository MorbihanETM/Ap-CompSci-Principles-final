from flask import Flask, request, redirect, render_template
from formula_one_quiz import FormulaOne

app = Flask(__name__)

driver_values = FormulaOne(0, 0, 0, 0)

IMG_DIR = './static'


# @app.route('/image')
# def serve_image():
#     "a simple HTTP image"
#     return render_template('image.html')

@app.route('/values')
def values():
    return list(driver_values.driver.items())

@app.route('/reset')
def reset():
    driver_values.clear()
    return 'the points have been reset!'

@app.route('/question/1', methods = ['GET', 'POST'])
def first_question():
    answers = ['angry', 'sad', 'happy', 'contemplative']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Max Verstappen')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
        if selected == answers[2]:
            driver_values.add('Lando Norris')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')

        return redirect('/question/2')

@app.route('/question/2', methods = ['GET', 'POST'])
def second_question():
    answers = ['on the dance floor', 'at a coffee shop', 'playing video games', 'at home']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Max Verstappen')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
        if selected == answers[2]:
            driver_values.add('Lando Norris')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')

        return redirect('/question/3')

@app.route('/question/3', methods = ['GET', 'POST'])
def third_question():
    answers = ['dark blue', 'bright red', 'papaya orange', 'emerald green']

    if request.method == 'GET':
        return render_template('question_3.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Max Verstappen')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
        if selected == answers[2]:
            driver_values.add('Lando Norris')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')

        return redirect('/question/4')

@app.route('/question/4', methods = ['GET', 'POST'])
def fourth_question():
    answers = ['relishing in the misery of your enemies', 'getting a coffee with a good book', 'making abstract art with loud music in your ears', 'taking a nap']

    if request.method == 'GET':
        return render_template('question_4.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Max Verstappen')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
        if selected == answers[2]:
            driver_values.add('Lando Norris')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')

        return redirect('/question/5')

@app.route('/question/5', methods = ['GET', 'POST'])
def fifth_question():
    answers = ['celebrity', 'architect', 'gamer', 'golfer']

    if request.method == 'GET':
        return render_template('question_5.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Max Verstappen')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
        if selected == answers[2]:
            driver_values.add('Lando Norris')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')
    
    return redirect('/genre')

@app.route('/genre')
def get_house():
    return 'congratulations, the formula 1 driver that most fits you right now is ' + driver_values.sort() + '!'

if __name__ == '__main__':
    app.run(host='localhost', port=8081)
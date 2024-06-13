from flask import Flask, request, redirect, render_template
from formula_one_quiz import FormulaOne

# Initiate web app with Flask
app = Flask(__name__)

# Define the starting values as 0
driver_values = FormulaOne(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Create web location that returns the cyrrent driver values
@app.route('/values')
def values():
    return list(driver_values.driver.items())

# Create web location that resets all driver values to 0
@app.route('/reset')
def reset():
    driver_values.clear()
    return 'the points have been reset!'

@app.route('/question/1', methods = ['GET', 'POST'])
def first_question():
# How are you feeling right now?
    answers = ['angry', 'sad', 'happy', 'contemplative']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Max Verstappen')
            driver_values.add('Esteban Ocon')
            driver_values.add('Kevin Magnussen')
            driver_values.add('Fernando Alonso')
            driver_values.add('Alexander Albon')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
            driver_values.add('Logan Sargeant')
            driver_values.add('Zhou Guanyu')
            driver_values.add('George Russell')
            driver_values.add('Lance Stroll')
        if selected == answers[2]:
            driver_values.add('Lando Norris')
            driver_values.add('Daniel Ricciardo')
            driver_values.add('Carlos Sainz')
            driver_values.add('Nico Hulkenberg')
            driver_values.add('Yuki Tsunoda')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')
            driver_values.add('Lewis Hamilton')
            driver_values.add('Valterri Bottas')
            driver_values.add('Pierre Gasly')
            driver_values.add('Oscar Piastri')
        return redirect('/question/2')

@app.route('/question/2', methods = ['GET', 'POST'])
def second_question():
# Where do you feel most comfortable?
    answers = ['on the dance floor', 'at a coffee shop', 'playing video games',
                'at the gym']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Max Verstappen')
            driver_values.add('Daniel Ricciardo')
            driver_values.add('Valterri Bottas')
            driver_values.add('Lando Norris')
            driver_values.add('Carlos Sainz')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
            driver_values.add('George Russell')
            driver_values.add('Oscar Piastri')
            driver_values.add('Yuki Tsunoda')
            driver_values.add('Alexander Albon')
        if selected == answers[2]:
            driver_values.add('Zhou Guanyu')
            driver_values.add('Esteban Ocon')
            driver_values.add('Sergio Perez')
            driver_values.add('Nico Hulkenberg')
            driver_values.add('Kevin Magnussen')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')
            driver_values.add('Pierre Gasly')
            driver_values.add('Lewis Hamilton')
            driver_values.add('Logan Sargeant')
            driver_values.add('Lance Stroll')

        return redirect('/question/3')

@app.route('/question/3', methods = ['GET', 'POST'])
def third_question():
# Which color do you prefer?
    answers = ['dark blue', 'bright red', 'papaya orange', 'emerald green']

    if request.method == 'GET':
        return render_template('question_3.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Max Verstappen')
            driver_values.add('Max')
            driver_values.add('Max')
            driver_values.add('Max')
            driver_values.add('Max')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
            driver_values.add('Max')
            driver_values.add('Max')
            driver_values.add('Max')
            driver_values.add('Max')
        if selected == answers[2]:
            driver_values.add('Lando Norris')
            driver_values.add('Max')
            driver_values.add('Max')
            driver_values.add('Max')
            driver_values.add('Max')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')
            driver_values.add('Max')
            driver_values.add('Max')
            driver_values.add('Max')
            driver_values.add('Max')

        return redirect('/question/4')

@app.route('/question/4', methods = ['GET', 'POST'])
def fourth_question():
# What do you prefer?
    answers = ['relishing in the misery of your enemies', 'getting a coffee with a good book', 'making abstract art with loud music in your ears', 'taking a nap']

    if request.method == 'GET':
        return render_template('question_4.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Max Verstappen')
            driver_values.add('Esteban Ocon')
            driver_values.add('Kevin Magnussen')
            driver_values.add('Yuki Tsunoda')
            driver_values.add('Oscar Piastri')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
            driver_values.add('George Russell')
            driver_values.add('Alexander Albon')
            driver_values.add('Zhou Guanyu')
            driver_values.add('Nico Hulkenberg')
        if selected == answers[2]:
            driver_values.add('')
            driver_values.add('Lewis Hamilton')
            driver_values.add('Logan Sargeant')
            driver_values.add('Valterri Bottas')
            driver_values.add('Pierre Gasly')
            driver_values.add('Daniel Ricciardo')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')
            driver_values.add('Lando Norris')
            driver_values.add('Lance Stroll')
            driver_values.add('Carlos Sainz')
            driver_values.add('Sergio Perez')

        return redirect('/question/5')

@app.route('/question/5', methods = ['GET', 'POST'])
def fifth_question():
# which profession do you prefer?
    answers = ['celebrity', 'architect', 'gamer', 'golfer']

    if request.method == 'GET':
        return render_template('question_5.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Daniel Ricciardo')
            driver_values.add('Carlos Sainz')
            driver_values.add('Esteban Ocon')
            driver_values.add('Fernando Alonso')
            driver_values.add('Lewis Hamilton')
        if selected == answers[1]:
            driver_values.add('Charles Leclerc')
            driver_values.add('Oscar Piastri')
            driver_values.add('Kevin Magnussen')
            driver_values.add('Alexander Albon')
            driver_values.add('Max Verstappen')
        if selected == answers[2]:
            driver_values.add('Lando Norris')
            driver_values.add('Lance Stroll')
            driver_values.add('Logan Sargeant')
            driver_values.add('Zhou Guanyu')
            driver_values.add('Yuki Tsunoda')
        if selected == answers[3]:
            driver_values.add('Fernando Alonso')
            driver_values.add('Valterri Bottas')
            driver_values.add('George Russell')
            driver_values.add('Sergio Perez')
            driver_values.add('Nico Hulkenberg')
    
        return redirect('/question/6')

@app.route('/question/6', methods = ['GET', 'POST'])
def sixth_question():
# What is your preferred love language?
    answers = ['gift giving' ,'quality time', 'physical touch', 'what is love?']

    if request.method == 'GET':
        return render_template('question_6.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Lewis Hamilton')
            driver_values.add('Charles Leclerc')
            driver_values.add('Nico Hulkenberg')
            driver_values.add('George Russell')
            driver_values.add('Fernando Alonso')
        if selected == answers[1]:
            driver_values.add('Carlos Sainz')
            driver_values.add('Pierre Gasly')
            driver_values.add('Logan Sargeant')
            driver_values.add('Zhou Guanyu')
            driver_values.add('Yuki Tsunoda')
        if selected == answers[2]:
            driver_values.add('Daniel Ricciardo')
            driver_values.add('Max Verstappen')
            driver_values.add('Lando Norris')
            driver_values.add('Alexander Albon')
            driver_values.add('Oscar Piastri')
        if selected == answers[3]:
            driver_values.add('Lance Stroll')
            driver_values.add('Valterri Bottas')
            driver_values.add('Kevin Magnussen')
            driver_values.add('Esteban Oon')
            driver_values.add('Sergio Perez')
    
    return redirect('/question/7')

@app.route('/question/7', methods = ['GET', 'POST'])
def seventh_question():
# WHat is your spirit animal?
    answers = ['Golden Retriever', 'Spider', 'Black Cat', 'Goldfish']

    if request.method == 'GET':
        return render_template('question_7.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Charles Leclerc')
            driver_values.add('Lando Norris')
            driver_values.add('Logan Sargeant')
            driver_values.add('Daniel Ricciardo')
            driver_values.add('Alexander Albon')
        if selected == answers[1]:
            driver_values.add('Carlos Sainz')
            driver_values.add('Fernando Alonso')
            driver_values.add('Esteban Ocon')
            driver_values.add('Oscar Piastri')
            driver_values.add('Sergio Perez')
        if selected == answers[2]:
            driver_values.add('Lewis Hamilton')
            driver_values.add('Max Verstappen')
            driver_values.add('Kevin Magnussen')
            driver_values.add('Nico Hulkenberg')
            driver_values.add('George Russell')
        if selected == answers[3]:
            driver_values.add('Yuki Tsunoda')
            driver_values.add('Valterri Bottas')
            driver_values.add('Pierre Gasly')
            driver_values.add('Zhou Guanyu')
            driver_values.add('Lance Stroll')
    
    return redirect('/question/8')
    
@app.route('/question/8', methods = ['GET', 'POST'])
def eighth_question():
# Whats the ideal home?
    answers = ['a cottage in the middle of nowhere','a new york city condo overlooking central park','a victorian style chateau','a sail boat',]

    if request.method == 'GET':
        return render_template('question_8.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            driver_values.add('Fernando Alonso')
            driver_values.add('Max Vertsappen')
            driver_values.add('Valterri Bottas')
            driver_values.add('Charles Leclerc')
            driver_values.add('Nico Hulkenberg')
        if selected == answers[1]:
            driver_values.add('Lewis Hamilton')
            driver_values.add('Daniel Ricciardo')
            driver_values.add('Carlos Sainz')
            driver_values.add('Lance Stroll')
            driver_values.add('Logan Sargeant')
        if selected == answers[2]:
            driver_values.add('Esteban Ocon')
            driver_values.add('Kevin Magnussen')
            driver_values.add('Oscar Piastri')
            driver_values.add('Sergio Perez')
            driver_values.add('George Russell')
        if selected == answers[3]:
            driver_values.add('Zhou Guanyu')
            driver_values.add('Yuki Tsunoda')
            driver_values.add('Pierre Gasly')
            driver_values.add('Lando Norris')
            driver_values.add('Alexander Albon')

    return redirect('/genre')

# Create web location that returns results
@app.route('/genre')
def get_house():
    return 'congratulations, the formula 1 driver that most fits you is ' + driver_values.sort() + '!'

if __name__ == '__main__':
    app.run(host='localhost', port=8081)
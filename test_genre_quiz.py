from formula_one_quiz import FormulaOne


def test_genre_quiz():
    quiz = FormulaOne(0,0,0,0)
    quiz.add('Max Verstappen')
    assert quiz.sort() == 'Max Verstappen'
    
def test_genre_quiz_equality():
    quiz = FormulaOne(1,1,1,0)
    assert quiz.sort() == 'electropop'
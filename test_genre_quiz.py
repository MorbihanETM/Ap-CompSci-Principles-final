from genre_quiz import GenreQuiz


def test_genre_quiz():
    quiz = GenreQuiz(0,0,0,0)
    quiz.add('pop')
    assert quiz.sort() == 'pop'
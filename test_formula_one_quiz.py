from formula_one_quiz import FormulaOne
import pytest
# from app import create_app

@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield client
    ctx.pop()

def test_final_page(client):
    response = client.get('/genre')
    assert response.status_code == 200

def test_genre_quiz():
    quiz = FormulaOne(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    quiz.add('Max Verstappen')
    assert quiz.sort() == 'Max Verstappen'
    
def test_genre_quiz_equality():
    quiz = FormulaOne(7, 3, 2, 2, 5, 5, 6, 1, 0, 0, 4, 0, 6, 0, 4, 0, 3, 2, 2, 0)
    assert quiz.sort() == 'Max Verstappen'
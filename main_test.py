import pytest
from main import app, posts


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_blog_overview(client):
    response = client.get('/posts')
    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_blog_detail(client):
    response = client.get('/posts/1')
    assert response.status_code == 200
    assert response.get_json()['title'] == 'Erster Beitrag'


def test_add_post(client):
    new_post = {'title': 'Dritter Beitrag', 'content': 'Dies ist der Inhalt des dritten Beitrags.'}
    response = client.post('/posts', json=new_post)
    assert response.status_code == 201
    assert response.get_json()['title'] == new_post['title']


def test_delete_post(client):
    # Zuerst die Anzahl der vorhandenen Beiträge überprüfen
    response = client.get('/posts')
    initial_count = len(response.get_json())

    # Einen Beitrag löschen
    response_delete = client.delete('/posts/1')
    assert response_delete.status_code == 200
    assert response_delete.get_json()['message'] == 'Post erfolgreich gelöscht'

    # Nach dem Löschen die Anzahl der Beiträge erneut überprüfen
    response_after_delete = client.get('/posts')
    assert len(response_after_delete.get_json()) == initial_count - 1

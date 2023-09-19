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
    response = client.delete('/posts/1')
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Post erfolgreich gelöscht'
    assert len(posts) == 1

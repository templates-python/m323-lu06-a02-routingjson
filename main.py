from flask import Flask, jsonify, request

app = Flask(__name__)

# Eine einfache Datenstruktur zur Speicherung der Blog-Beiträge
posts = [
    {'id': 1, 'title': 'Erster Beitrag', 'content': 'Dies ist der Inhalt des ersten Beitrags.'},
    {'id': 2, 'title': 'Zweiter Beitrag', 'content': 'Dies ist der Inhalt des zweiten Beitrags.'}
]

@app.route('/posts', methods=['GET'])
def blog_overview():
    """Gibt eine Übersicht aller Blog-Beiträge als JSON zurück."""
    return jsonify(posts)

@app.route('/posts/<int:post_id>', methods=['GET'])
def blog_detail(post_id):
    """Gibt die Details eines bestimmten Blog-Beitrags als JSON zurück."""
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post)
    return jsonify({'message': 'Post nicht gefunden'}), 404

@app.route('/posts', methods=['POST'])
def add_post():
    """Fügt einen neuen Blog-Beitrag hinzu und gibt diesen als JSON zurück."""
    data = request.get_json()
    new_post = {
        'id': len(posts) + 1,
        'title': data['title'],
        'content': data['content']
    }
    posts.append(new_post)
    return jsonify(new_post), 201

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """Löscht einen bestimmten Blog-Beitrag und gibt eine Bestätigungsnachricht zurück."""
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return jsonify({'message': 'Post erfolgreich gelöscht'}), 200

if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request

app = Flask(__name__)

# Eine einfache Datenstruktur zur Speicherung der Blog-Beiträge
posts = [
    {'id': 1, 'title': 'Erster Beitrag', 'content': 'Dies ist der Inhalt des ersten Beitrags.'},
    {'id': 2, 'title': 'Zweiter Beitrag', 'content': 'Dies ist der Inhalt des zweiten Beitrags.'}
]


def blog_overview():
    """Gibt eine Übersicht aller Blog-Beiträge als JSON zurück."""
    pass


def blog_detail(post_id):
    """Gibt die Details eines bestimmten Blog-Beitrags als JSON zurück."""
    pass


def add_post():
    """Fügt einen neuen Blog-Beitrag hinzu und gibt diesen als JSON zurück."""
    pass


def delete_post(post_id):
    """Löscht einen bestimmten Blog-Beitrag und gibt eine Bestätigungsnachricht zurück."""
    pass


if __name__ == '__main__':
    app.run()
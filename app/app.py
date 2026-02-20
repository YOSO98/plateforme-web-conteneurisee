from flask import Flask
import socket
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now()

    return f"""
    <h1>Plateforme Web Conteneurisée</h1>
    <p><strong>Statut :</strong> Application opérationnelle</p>
    <p><strong>Hostname :</strong> {hostname}</p>
    <p><strong>Date & heure :</strong> {current_time}</p>
    <p><strong>Environnement :</strong> {os.getenv('ENV', 'local')}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

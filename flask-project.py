from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    r = requests.get('https://fantasy.premierleague.com/drf/leagues-classic-standings/27032')
    leaderboard = r.json()['standings']['results']
    return render_template('index.html', leaderboard=leaderboard)

if __name__ == '__main__':
    app.run()

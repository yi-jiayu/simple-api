import requests

r = requests.get('https://fantasy.premierleague.com/drf/leagues-classic-standings/27032')
leaderboard = r.json()['standings']['results']

for item in leaderboard:
    print(item['player_name'], item['total'])

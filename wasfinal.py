
import requests

def getDate():

    date = input("Enter date (YYYY-MM-DD): ")

    y = date[0:4]
    m = date[5:7]
    d = date[8:]
    return y,m,d

y,m,d = getDate()

r = requests.get(f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={m}%2F{d}%2F{y}")


res = r.json()

games = res['dates'][0]['games']

for i in range(0, len(games)):
    awayTeamName = games[i]['teams']['away']['team']['name']
    homeTeamName = games[i]['teams']['home']['team']['name']
    print(f"{i+1}. {awayTeamName} at {homeTeamName}")

chosen = input('select game to check: ')

chosenId = games[int(chosen)-1]['gamePk']

g = requests.get(f"https://statsapi.mlb.com/api/v1/game/{chosenId}/boxscore")
game = g.json()
homeScore = game['teams']['home']['teamStats']['batting']['runs']
awayScore = game['teams']['away']['teamStats']['batting']['runs']

guess = input("enter score (away-home): ")
print("\n")
if guess == f"{awayScore}-{homeScore}":
    print("that was the final score.")
else:
    print("not the final score")

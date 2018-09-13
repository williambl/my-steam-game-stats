import requests
from os import environ
from datetime import datetime

key = environ["STEAM_API_KEY"]
steamid = environ["STEAM_ID"]

r = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={steamid}&format=json")

games = r.json()["response"]["games"]
games_played = [game for game in games if game["playtime_forever"] > 0]
releaseyears = []

for game in games_played:
    appid = game["appid"]

    r = requests.get(f"https://store.steampowered.com/api/appdetails?appids={appid}&filters=release_date")

    try:
        release_date = r.json()[str(appid)]["data"]["release_date"]["date"]
        release_year = datetime.strptime(release_date, "%d %b, %Y").year
        releaseyears.append(release_year)
    except:
        print("error with appid " + str(appid))


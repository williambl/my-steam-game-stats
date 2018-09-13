import requests
from datetime import datetime

key = ""
steamid = ""

r = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={steamid}&format=json")

games = r.json()["response"]["games"]
releaseyears = []

for game in games:
    if (game["playtime_forever"] > 0):
        appid = game["appid"]
        r = requests.get(f"https://store.steampowered.com/api/appdetails?appids={appid}&filters=release_date")
        release_date = r.json()[str(appid)]["data"]["release_date"]["date"]
        release_year = datetime.strptime(release_date, "%d %b, %Y").year
        print(release_year)
        releaseyears.append(release_year)

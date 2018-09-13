import requests

key = ""
steamid = ""

r = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={steamid}&format=json")

games = r.json()["response"]["games"]

for game in games:
    print(game)
    if (game["playtime_forever"] > 0):
        appid = game["appid"]
        r = requests.get(f"https://store.steampowered.com/api/appdetails?appids={appid}&filters=release_date")
        print(r.json())

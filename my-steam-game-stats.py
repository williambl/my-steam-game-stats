import requests

key = ""
steamid = ""

r = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={steamid}&format=json")

print(r.json())

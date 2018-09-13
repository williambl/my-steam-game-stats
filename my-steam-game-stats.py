import requests

key = ""
steamid = ""

r = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+key"&steamid="+steamid+"&format=json")

print(r.json())

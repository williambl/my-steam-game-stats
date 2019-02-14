import requests
from os import environ
from datetime import datetime
from progress.bar import Bar
import collections
from matplotlib import pyplot

key = environ["STEAM_API_KEY"]
steamid = environ["STEAM_ID"]

r = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={steamid}&format=json")

games = r.json()["response"]["games"]
games_played = [game for game in games if game["playtime_forever"] > 0]
releaseyears = []
publishers = []

bar = Bar('Getting Release Dates', max=games_played.__len__())
for game in games_played:
    appid = game["appid"]

    r = requests.get(f"https://store.steampowered.com/api/appdetails?appids={appid}&filters=release_date,publishers")

    try:
        release_date = r.json()[str(appid)]["data"]["release_date"]["date"]
        release_year = datetime.strptime(release_date, "%d %b, %Y").year
        releaseyears.append(release_year)
    except:
        print("error with appid " + str(appid) + " release date")

    try:
        publisher = r.json()[str(appid)]["data"]["publishers"][0]
        publishers.append(publisher)
    except:
        print("error with appid " + str(appid) + " publishers")


    bar.next()
bar.finish()

year_frequencies = collections.Counter(releaseyears)
print(year_frequencies)

publisher_frequencies = collections.Counter(publishers)
other = 0
others = []
for pub, val in publisher_frequencies.items():
    if (val == 1):
        others.append(pub)
        other += 1
if (other > 0):
    for pub in others:
        del publisher_frequencies[pub]
    publisher_frequencies["Other"] = other
print(publisher_frequencies)

pyplot.figure(1)
pyplot.bar(year_frequencies.keys(), year_frequencies.values())
pyplot.savefig("year_frequencies.svg")
pyplot.figure(2)
pyplot.bar(publisher_frequencies.keys(), publisher_frequencies.values())
pyplot.savefig("publisher_frequencies.svg")
pyplot.show()

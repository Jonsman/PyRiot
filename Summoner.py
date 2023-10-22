import requests
import os
import json


class Summoner:
    def __init__(self, name, tag):
        self.name = name
        self.tag = tag
        self.puuid = ""
        self.id = ""

    def getPuuid(self):
        response = requests.get(
            "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"
            + self.name
            + "/"
            + self.tag
            + "?api_key="
            + os.getenv("API_KEY")
        )

        self.puuid = response.json()["puuid"]

        with open("./Data/summonerPuuid.json", "w") as file:
            json.dump(response.json(), file, indent=4)

    def getId(self):
        response = requests.get(
            "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"
            + self.puuid
            + "?api_key="
            + os.getenv("API_KEY")
        )

        self.id = response.json()["id"]

        with open("./Data/summonerId.json", "w") as file:
            json.dump(response.json(), file, indent=4)

    def getRankedData(self):
        response = requests.get(
            "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/"
            + self.id
            + "?api_key="
            + os.getenv("API_KEY")
        )

        with open("./Data/summonerRankedData.json", "w") as file:
            json.dump(response.json(), file, indent=4)

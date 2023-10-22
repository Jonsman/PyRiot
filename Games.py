import requests
import json
import os


class Games:
    def __init__(self):
        pass

    def getMatchHistory(self, summoner):
        response = requests.get(
            "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
            + summoner.puuid
            + "/ids?api_key="
            + os.getenv("API_KEY")
        )

        self.getMatchHistory = response.json()

        with open("lastGames.json", "w") as file:
            json.dump(response.json(), file, indent=4)

    def getMatchData(self, input):
        response = requests.get(
            "https://europe.api.riotgames.com/lol/match/v5/matches/"
            + input
            + "?api_key="
            + os.getenv("API_KEY")
        )

        with open("./Matches/" + input + ".json", "w") as file:
            json.dump(response.json(), file, indent=4)

    def getMatchHistoryData(self):
        for x in self.getMatchHistory:
            self.getMatchData(x)

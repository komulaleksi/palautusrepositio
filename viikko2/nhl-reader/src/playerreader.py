from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        import requests
        response = requests.get(self.url).json()
        players = [Player(player_dict) for player_dict in response]
        return players
import requests

from player import Player


# A reader deliberately exposes a single operation to its consumer.
# pylint: disable=too-few-public-methods
class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        return [Player(player_data) for player_data in response.json()]

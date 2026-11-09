import unittest
from unittest.mock import Mock

from src.player import Player
from src.playerstats import PlayerStats


class PlayerStatsTest(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player({
                "name": "Alex",
                "nationality": "FIN",
                "team": "TOR",
                "goals": 10,
                "assists": 20,
            }),
            Player({
                "name": "Blake",
                "nationality": "CAN",
                "team": "TOR",
                "goals": 15,
                "assists": 18,
            }),
            Player({
                "name": "Casey",
                "nationality": "FIN",
                "team": "BOS",
                "goals": 5,
                "assists": 10,
            }),
        ]
        self.reader = Mock()
        self.reader.get_players.return_value = self.players
        self.stats = PlayerStats(self.reader)

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player.name for player in result], ["Alex", "Casey"])
        self.reader.get_players.assert_called_once_with()

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("TOR")

        self.assertEqual([player.name for player in result], ["Blake", "Alex"])
        self.reader.get_players.assert_called_once_with()

    def test_top_scorers_by_team_returns_empty_list_when_team_has_no_players(self):
        result = self.stats.top_scorers_by_team("MTL")

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()

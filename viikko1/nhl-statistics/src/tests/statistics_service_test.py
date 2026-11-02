import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class StubPlayerReader:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player("Aleksander Barkov", "FLA", 20, 30),
            Player("Mikko Rantanen", "COL", 30, 40),
            Player("Nathan MacKinnon", "COL", 40, 50),
        ]
        self.statistics = StatisticsService(StubPlayerReader(self.players))

    def test_search_returns_player_whose_name_contains_search_term(self):
        self.assertIs(self.statistics.search("Mikko"), self.players[1])

    def test_search_returns_none_when_no_player_matches(self):
        self.assertIsNone(self.statistics.search("Connor"))

    def test_team_returns_players_from_exact_team(self):
        self.assertEqual(
            self.statistics.team("COL"),
            [self.players[1], self.players[2]],
        )

    def test_team_returns_empty_list_when_team_has_no_players(self):
        self.assertEqual(self.statistics.team("BOS"), [])

    def test_top_returns_requested_number_of_players_by_points(self):
        self.assertEqual(
            self.statistics.top(2),
            [self.players[2], self.players[1]],
        )

    def test_top_returns_empty_list_when_zero_players_are_requested(self):
        self.assertEqual(self.statistics.top(0), [])

    def test_top_returns_all_players_when_request_exceeds_roster(self):
        self.assertEqual(
            self.statistics.top(10),
            [self.players[2], self.players[1], self.players[0]],
        )

    def test_top_can_sort_by_goals(self):
        players = [
            Player("Assist leader", "AAA", 10, 100),
            Player("Goal leader", "BBB", 50, 0),
            Player("Balanced player", "CCC", 20, 20),
        ]
        statistics = StatisticsService(StubPlayerReader(players))

        self.assertEqual(
            statistics.top(3, SortBy.GOALS),
            [players[1], players[2], players[0]],
        )

    def test_top_can_sort_by_assists(self):
        players = [
            Player("Assist leader", "AAA", 10, 100),
            Player("Goal leader", "BBB", 50, 0),
            Player("Balanced player", "CCC", 20, 20),
        ]
        statistics = StatisticsService(StubPlayerReader(players))

        self.assertEqual(
            statistics.top(3, SortBy.ASSISTS),
            [players[0], players[2], players[1]],
        )

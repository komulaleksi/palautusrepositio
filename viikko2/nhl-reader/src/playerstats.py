class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered_players = [player for player in players if player.nationality == nationality]
        sorted_players = sorted(filtered_players, key=lambda player: player.points, reverse=True)
        return sorted_players

    def top_scorers_by_team(self, team):
        players = self.reader.get_players()
        filtered_players = [player for player in players if player.team == team]
        sorted_players = sorted(filtered_players, key=lambda player: player.points, reverse=True)
        return sorted_players

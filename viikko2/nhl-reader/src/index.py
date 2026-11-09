from playerreader import PlayerReader
from playerstats import PlayerStats


def _choose_grouping():
    while True:
        selection = input("Show players by (n)ationality or (t)eam? ").strip().lower()
        if selection in ("n", "t"):
            break
        print("Please enter 'n' for nationality or 't' for team.")
    return selection


def _get_ranked_players(stats, selection):
    if selection == "n":
        value = input("Nationality code (for example FIN): ").strip().upper()
        players = stats.top_scorers_by_nationality(value)
        description = f"nationality {value}"
    else:
        value = input("Team code (for example TOR): ").strip().upper()
        players = stats.top_scorers_by_team(value)
        description = f"team {value}"
    return players, description


def _print_players(players, description, season):
    if not players:
        print(f"No players found for {description} in {season}.")
        return

    print(f"Top scorers for {description} in {season}:")
    for rank, player in enumerate(players, start=1):
        print(f"{rank}. {player}")


def main():
    season = input("Season (for example 2024-25): ").strip()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    selection = _choose_grouping()
    players, description = _get_ranked_players(stats, selection)
    _print_players(players, description, season)


if __name__ == "__main__":
    main()

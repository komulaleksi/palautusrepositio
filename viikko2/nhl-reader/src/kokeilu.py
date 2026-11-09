from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2026-27/players"
    stats = PlayerStats(PlayerReader(url))

    for p in stats.top_scorers_by_team("DAL"):
        print(p)

if __name__ == "__main__":
    main()

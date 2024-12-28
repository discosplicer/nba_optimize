

teams = [
    {"franchise": "Golden State Warriors", "overall": 85, "year": 2017, "players": ["Kevin Durant", "Stephen Curry", "Klay Thompson", "Draymond Green"]},
    {"franchise": "Los Angeles Lakers", "overall": 85, "year": 1987, "players": ["Magic Johnson", "Kareem Abdul-Jabbar", "James Worthy", "Michael Cooper"]},
    {"franchise": "Chicago Bulls", "overall": 84, "year": 1996, "players": ["Michael Jordan", "Scottie Pippen", "Dennis Rodman"]},
    {"franchise": "Golden State Warriors", "overall": 84, "year": 2016, "players": ["Stephen Curry", "Klay Thompson", "Draymond Green"]},
    {"franchise": "Boston Celtics", "overall": 84, "year": 1986, "players": ["Larry Bird", "Kevin McHale", "Robert Parish"]},
    {"franchise": "San Antonio Spurs", "overall": 83, "year": 2014, "players": ["Tim Duncan", "Kawhi Leonard", "Tony Parker"]},
    {"franchise": "San Antonio Spurs", "overall": 83, "year": 2005, "players": ["Tim Duncan", "Tony Parker", "Manu Ginobli"]},
    {"franchise": "Los Angeles Clippers", "overall": 83, "year": 2014, "players": ["Chris Paul", "DeAndre Jordan"]},
    {"franchise": "Toronto Raptors", "overall": 83, "year": 2019, "players": ["Kawhi Leonard", "Pascal Siakam", "Kyle Lowry"]},
    {"franchise": "Boston Celtics", "overall": 83, "year": 2008, "players": ["Kevin Garnett", "Paul Pierce", "Ray Allen", "Rajon Rondo"]},
    {"franchise": "Dallas Mavericks", "overall": 83, "year": 2011, "players": ["Dirk Nowitzki"]},
    {"franchise": "Oklahoma City Thunder", "overall": 82, "year": 2012, "players": ["Kevin Durant", "Russell Westbrook", "James Harden"]},
    {"franchise": "Cleveland Cavaliers", "overall": 82, "year": 2016, "players": ["LeBron James", "Kyrie Irving", "Kevin Love"]},
    {"franchise": "Miami Heat", "overall": 82, "year": 2013, "players": ["LeBron James", "Dwyane Wade", "Chris Bosh"]},
    {"franchise": "Detroit Pistons", "overall": 82, "year": 1989, "players": ["Isiah Thomas", "Joe Dumars"]},
    {"franchise": "Sacramento Kings", "overall": 82, "year": 2002, "players": ["Chris Webber", "Peja Stojakovic", "Vlade Divac"]},
    {"franchise": "Los Angeles Lakers", "overall": 82, "year": 2001, "players": ["Kobe Bryant", "Shaquille O'Neal"]},
    {"franchise": "Chicago Bulls", "overall": 82, "year": 2011, "players": ["Derrick Rose", "Joakim Noah", "Carlos Boozer"]},
    {"franchise": "Portland Trail Blazers", "overall": 82, "year": 2010, "players": ["Brandon Roy", "LaMarcus Aldridge"]},
    {"franchise": "Denver Nuggets", "overall": 81, "year": 2008, "players": ["Allen Iverson", "Carmelo Anthony", "Marcus Camby"]},
    {"franchise": "New York Knicks", "overall": 81, "year": 2012, "players": ["Carmelo Anthony", "Amare Stoudemire"]},
    {"franchise": "Washington Wizards", "overall": 81, "year": 2007, "players": ["Gilbert Arenas", "Antawn Jamison", "Caron Butler"]},
    {"franchise": "Chicago Bulls", "overall": 81, "year": 1993, "players": ["Michael Jordan", "Scottie Pippen"]},
    {"franchise": "Miami Heat", "overall": 81, "year": 1997, "players": ["Alonzo Mourning", "Tim Hardaway"]},
    {"franchise": "Phoenix Suns", "overall": 81, "year": 2005, "players": ["Steve Nash", "Amare Stoudemire", "Shawn Marion"]},
    {"franchise": "Portland Trail Blazers", "overall": 81, "year": 1991, "players": ["Clyde Drexler", "Terry Porter"]},
    {"franchise": "Utah Jazz", "overall": 81, "year": 1991, "players": ["Karl Malone", "John Stockton"]},
    {"franchise": "Miami Heat", "overall": 81, "year": 2006, "players": ["Dwayne Wade", "Shaquille O'Neal"]},
    {"franchise": "Dallas Mavericks", "overall": 81, "year": 2003, "players": ["Dirk Nowitzki", "Steve Nash"]},
]
for team in teams:
    team["name"] = f"{team['year']} {team['franchise']}"

def maximize_teams_dp(teams):
    from functools import lru_cache

    # Preprocess the list of players and franchises into unique indices for bitmasking
    franchise_map = {team["franchise"]: i for i, team in enumerate({team["franchise"] for team in teams})}
    player_map = {player: i for i, player in enumerate({player for team in teams for player in team["players"]})}

    # Encode each team as a dictionary with bitmasks for franchise and players
    encoded_teams = []
    for team in teams:
        franchise_mask = 1 << franchise_map[team["franchise"]]
        player_mask = sum(1 << player_map[player] for player in team["players"])
        encoded_teams.append({
            "overall": team["overall"],
            "franchise_mask": franchise_mask,
            "player_mask": player_mask,
            "original_team": team
        })

    # Memoization cache
    @lru_cache(None)
    def dp(index, used_franchises, used_players):
        # Base case: no more teams to consider
        if index == len(encoded_teams):
            return 0, []

        # Skip the current team
        max_score, selected_teams = dp(index + 1, used_franchises, used_players)

        # Try including the current team if it doesn't conflict
        team = encoded_teams[index]
        if (team["franchise_mask"] & used_franchises == 0) and (team["player_mask"] & used_players == 0):
            new_score, new_selection = dp(
                index + 1,
                used_franchises | team["franchise_mask"],
                used_players | team["player_mask"]
            )
            new_score += team["overall"]

            # Update the maximum score and selection
            if new_score > max_score:
                max_score = new_score
                selected_teams = [team["original_team"]] + new_selection

        return max_score, selected_teams

    # Start DP with no franchises or players used
    max_score, best_selection = dp(0, 0, 0)
    return best_selection

result = maximize_teams_dp(teams)
print("Selected Teams:")
for team in result:
    print(team)     
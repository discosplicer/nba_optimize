# WARNING VERY SLOW

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

def maximize_teams_backtrack(teams):
    def backtrack(index, current_score, used_teams, used_players, current_selection, max_team_count):
        nonlocal max_score, best_selection
        
        # Update the best score and selection if the current score is higher
        used_franchises = set(team["franchise"] for team in used_teams)
        overall_score = current_score + len(used_franchises) + len(used_players)

        if overall_score > max_score:
            max_score = overall_score
            best_selection = list(current_selection)  # Copy the current selection
        
        # Base case: if all teams have been considered
        if index == len(teams):
            return
        
        for i in range(index, len(teams)):
            team = teams[i]
            
            # Skip if the team or any player is already used
            if team in used_teams or any(player in used_players for player in team["players"]):
                continue
            
            # Skip if already at the max # of teams.
            if len(current_selection) >= max_team_count:
                continue

            # Include this team
            used_teams.append(team)
            used_players.update(team["players"])
            current_selection.append(team)
            
            # Recur to the next team
            backtrack(
                i + 1,
                current_score + team["overall"],
                used_teams,
                used_players,
                current_selection,
                max_team_count
            )
            
            # Backtrack (undo the choice)
            used_teams.pop()
            used_players.difference_update(team["players"])
            current_selection.pop()
        
        # Explore the case where the current team is skipped
        backtrack(index + 1, current_score, used_teams, used_players, current_selection, max_team_count)
    
    # Sort the teams by overall rating to help prioritize higher-rated teams first
    teams.sort(key=lambda x: x["overall"], reverse=True)
    
    # Initialize variables
    max_score = 0
    max_team_count = 16
    best_selection = []
    used_teams = []
    used_players = set()
    current_selection = []
    
    # Start the backtracking process
    backtrack(0, 0, used_teams, used_players, current_selection, max_team_count)
    
    return best_selection

result = maximize_teams_backtrack(teams)
print("Selected Teams:")
for team in result:
    print(team)     
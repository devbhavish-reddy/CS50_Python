with open("students.csv") as file:
    a = sorted(file, reverse=False)
    for line in a: 
        name, team = line.rstrip().split(",")
        print(f"Name is {name}, team is {team}")

players = []



with open("students.csv") as file: 
    for i in file: 

        name, team = i.rstrip().split(",")
        player = {"name": name, "team": team}
        players.append(player)

def player_name(player): 
    return player["name"]


players = sorted(players, key = player_name)


for pla in players: 
    print(f"{pla['name']} is in {pla['team']}")
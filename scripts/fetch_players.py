import json
import os

players = [
{"name":"Virat Kohli","team":"RCB"},
{"name":"MS Dhoni","team":"CSK"},
{"name":"Rohit Sharma","team":"MI"},
{"name":"Hardik Pandya","team":"MI"},
{"name":"Jasprit Bumrah","team":"MI"},
{"name":"Ravindra Jadeja","team":"CSK"},
{"name":"KL Rahul","team":"LSG"},
{"name":"Shubman Gill","team":"GT"}
]

os.makedirs("../data", exist_ok=True)

with open("../data/ipl_players.json","w") as f:
    json.dump(players,f,indent=4)

print("Players saved")
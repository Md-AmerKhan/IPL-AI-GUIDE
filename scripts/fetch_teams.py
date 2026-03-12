import json
import os

teams = [
{"name":"Mumbai Indians","short":"MI"},
{"name":"Chennai Super Kings","short":"CSK"},
{"name":"Royal Challengers Bengaluru","short":"RCB"},
{"name":"Kolkata Knight Riders","short":"KKR"},
{"name":"Sunrisers Hyderabad","short":"SRH"},
{"name":"Delhi Capitals","short":"DC"},
{"name":"Punjab Kings","short":"PBKS"},
{"name":"Rajasthan Royals","short":"RR"},
{"name":"Lucknow Super Giants","short":"LSG"},
{"name":"Gujarat Titans","short":"GT"}
]

os.makedirs("../data", exist_ok=True)

with open("../data/ipl_teams.json","w") as f:
    json.dump(teams,f,indent=4)

print("Teams saved")
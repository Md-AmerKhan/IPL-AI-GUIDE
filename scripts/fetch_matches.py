import requests
import json
import os

url = "https://api.cricapi.com/v1/matches?apikey=demo&offset=0"

response = requests.get(url)
data = response.json()

matches = []

for match in data.get("data", []):
    match_data = {
        "team1": match.get("teams", [None, None])[0],
        "team2": match.get("teams", [None, None])[1],
        "date": match.get("date"),
        "status": match.get("status"),
        "venue": match.get("venue")
    }

    matches.append(match_data)

os.makedirs("../data", exist_ok=True)

with open("../data/ipl_matches.json", "w") as f:
    json.dump(matches, f, indent=4)

print("Matches downloaded")
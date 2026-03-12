from flask import Flask, request, jsonify
import json
from rapidfuzz import process

app = Flask(__name__)

# Load data
with open("../data/ipl_matches.json") as f:
    matches = json.load(f)

with open("../data/ipl_teams.json") as f:
    teams = json.load(f)

with open("../data/ipl_players.json") as f:
    players = json.load(f)


team_names = [t["name"] for t in teams]
player_names = [p["name"] for p in players]


@app.route("/")
def home():
    return {
        "message":"IPL AI Guide Running",
        "usage":"Use /ask?q=your_question"
    }

@app.route("/ask")
def ask():

    question = request.args.get("q","").lower()

    # detect player
    player_match = process.extractOne(question, player_names)

    if player_match and player_match[1] > 80:
        player = player_match[0]

        for p in players:
            if p["name"] == player:
                return jsonify({
                    "answer": f"{player} plays for {p['team']} in IPL."
                })

    # detect team
    team_match = process.extractOne(question, team_names)

    if team_match and team_match[1] > 80:
        team = team_match[0]

        team_matches = [
            m for m in matches
            if team in (m.get("team1","") + m.get("team2",""))
        ]

        if team_matches:
            next_match = team_matches[0]

            return jsonify({
                "answer": f"Next match of {team} is {next_match['team1']} vs {next_match['team2']} on {next_match['date']} at {next_match['venue']}."
            })

    return jsonify({
        "answer":"Sorry, I couldn't find that IPL info."
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
from flask import Flask, request, jsonify
import json
import os
from rapidfuzz import process

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "data/ipl_matches.json")) as f:
    matches = json.load(f)

with open(os.path.join(BASE_DIR, "data/ipl_players.json")) as f:
    players = json.load(f)

with open(os.path.join(BASE_DIR, "data/ipl_teams.json")) as f:
    teams = json.load(f)

team_names = [t["name"] for t in teams]
player_names = [p["name"] for p in players]


@app.route("/")
def home():
    return {
        "message": "IPL AI Guide Running",
        "endpoint": "/ask?q=your_question"
    }


@app.route("/ask")
def ask():

    question = request.args.get("q", "").lower()

    # Detect player
    player_match = process.extractOne(question, player_names)

    if player_match and player_match[1] > 80:
        player = player_match[0]

        for p in players:
            if p["name"] == player:
                return jsonify({
                    "answer": f"{player} plays for {p['team']} in IPL."
                })

    # Detect team
    team_match = process.extractOne(question, team_names)

    if team_match and team_match[1] > 80:

        team = team_match[0]

        for m in matches:
            if team in [m["team1"], m["team2"]]:
                return jsonify({
                    "answer": f"Next match of {team} is {m['team1']} vs {m['team2']} on {m['date']} at {m['venue']}."
                })

    return jsonify({
        "answer": "Sorry, I couldn't find that IPL information."
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
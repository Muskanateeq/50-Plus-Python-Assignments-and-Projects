from flask import Flask, request  # ✅ Added request here
from flask_socketio import SocketIO, emit
import eventlet

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

players = {}

@socketio.on("connect")
def handle_connect():
    if len(players) < 2:
        players[request.sid] = {"y": 250, "score": 0}  # ✅ request is now defined
        emit("player_id", len(players), room=request.sid)
        emit("update_players", players, broadcast=True)
    else:
        emit("room_full", room=request.sid)

@socketio.on("move_paddle")
def move_paddle(data):
    if request.sid in players:
        players[request.sid]["y"] = data["y"]
        emit("update_players", players, broadcast=True)

@socketio.on("disconnect")
def handle_disconnect():
    if request.sid in players:
        del players[request.sid]
    emit("update_players", players, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)

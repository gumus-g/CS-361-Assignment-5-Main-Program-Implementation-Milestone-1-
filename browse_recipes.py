import zmq
import json

def browse_recipes():
    # Example recipe data
    recipes = [
        {"id": 1, "name": "Spaghetti Carbonara", "cuisine": "Italian"},
        {"id": 2, "name": "Tacos", "cuisine": "Mexican"},
        {"id": 3, "name": "Sushi", "cuisine": "Japanese"}
    ]
    return json.dumps(recipes)

# ZeroMQ context and socket setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Browse Recipes Server is running...")

while True:
    message = socket.recv()
    if message.decode() == "browse":
        recipes = browse_recipes()
        socket.send_string(recipes)


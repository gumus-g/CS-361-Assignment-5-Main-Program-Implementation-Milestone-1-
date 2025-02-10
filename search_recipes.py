import zmq
import json

# Example recipe data
recipes = [
    {"id": 1, "name": "Spaghetti Carbonara", "cuisine": "Italian"},
    {"id": 2, "name": "Tacos", "cuisine": "Mexican"},
    {"id": 3, "name": "Sushi", "cuisine": "Japanese"}
]

def search_recipes(keyword):
    return json.dumps([recipe for recipe in recipes if keyword.lower() in recipe["name"].lower()])

# ZeroMQ context and socket setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

print("Search Recipes Server is running...")

while True:
    message = socket.recv_string()
    search_result = search_recipes(message)
    socket.send_string(search_result)
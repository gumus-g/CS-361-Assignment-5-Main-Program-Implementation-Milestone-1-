import zmq
import json

# Example detailed recipe data
recipe_details = {
    1: {"name": "Spaghetti Carbonara", "ingredients": ["Spaghetti", "Eggs", "Parmesan", "Pancetta"], "steps": ["Boil pasta", "Fry pancetta", "Mix eggs and cheese", "Combine all"]},
    2: {"name": "Tacos", "ingredients": ["Tortillas", "Chicken", "Salsa", "Cheese"], "steps": ["Cook chicken", "Warm tortillas", "Assemble tacos"]},
    3: {"name": "Sushi", "ingredients": ["Rice", "Nori", "Fish", "Wasabi"], "steps": ["Cook rice", "Slice fish", "Roll sushi"]}
}

def view_recipe_details(recipe_id):
    return json.dumps(recipe_details.get(recipe_id, {}))

# ZeroMQ context and socket setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

print("View Recipe Server is running...")

while True:
    message = socket.recv_string()
    recipe_id = int(message)
    details = view_recipe_details(recipe_id)
    socket.send_string(details)
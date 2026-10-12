# List of percepts to test the room light agent
percept_sequence = ["Dark", "Dim", "Bright", "Dark"]

# Function to determine action based on the percept
def room_light_agent(percept):
    if percept == "Dark":
        return "Turn Light ON"
    elif percept == "Bright":
        return "Turn Light OFF"
    elif percept == "Dim":
        return "Leave Light As Is"
    else:
        return "Unknown Percept"

# Print the percepts and their corresponding actions
print(" ")
print("Percept ----- Action")
print("---------------------")
for percept in percept_sequence:
    action = room_light_agent(percept)
    print(f"{percept} ----- {action}")
print(" ")
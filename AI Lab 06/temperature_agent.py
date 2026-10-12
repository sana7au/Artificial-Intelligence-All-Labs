# Given sequence of percepts
percept_sequence = [
    ("Room1", "Cold"),
    ("Room1", "Normal"),
    ("Room2", "Hot"),
    ("Room2", "Normal"),
    ("Room1", "Cold")
]

# Store the last known reading of each room
model = {"Room1": None, "Room2": None}

# Count how many times the heater is turned ON in each room
heater_count = {"Room1": 0, "Room2": 0}

# Update the internal model with the latest reading
def update_model(room, reading):
    model[room] = reading

# Model-based temperature agent
def temperature_agent(room, reading):
    update_model(room, reading)

    # Turn the heater ON if the room is cold
    if reading == "Cold":
        heater_count[room] += 1
        return "Turn Heater ON"

    # Turn the heater OFF if the room is hot
    elif reading == "Hot":
        return "Turn Heater OFF"

    # Check whether both rooms have normal temperature
    elif model["Room1"] == "Normal" and model["Room2"] == "Normal":
        return "All Rooms Comfortable - Idle"

    # Otherwise, check the other room
    else:
        return "Move to Other Room to Check"

# Display the headings
print("Room\tReading\tAction\t\t\tInternal Model")
print("--------------------------------------------------------------")

# Process each room and its temperature reading
for room, reading in percept_sequence:
    action = temperature_agent(room, reading)

    # Display the action and updated model
    print(f"{room}\t{reading}\t{action}\t{model}")

# Display the total heater ON count for each room
print("\nHeater ON count:", heater_count)

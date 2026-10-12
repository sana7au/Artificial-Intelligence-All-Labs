# Table mapping traffic light colors to actions + flashing light percept added
table = {"Red": "Stop", "Yellow": "Slow Down", "Green": "Go", "Flashing Red": "Stop and proceed with caution"}

# List of percepts to test the traffic light agent
percept_sequence = ["Red", "Green", "Yellow", "Red", "Flashing Red"]

# Function to determine the action based on the percept
def traffic_light_agent(percept):
    return table.get(percept)

# Print the percepts and their actions
print(" ")
print("Percept ----- Action")
print("---------------------")
for percept in percept_sequence:
    action = traffic_light_agent(percept)
    print(f"{percept} ----- {action}")
print(" ")
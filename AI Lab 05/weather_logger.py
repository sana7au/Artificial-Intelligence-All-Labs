# List to store the temperatures entered by the user
temperatures = []

# Function to summarize the temperatures and return a dictionary
def summarize(temps):
    if len(temperatures) == 0:
        return {"minimum": None, "maximum": None, "average": None}
    else:
        minimum = min(temps)
        maximum = max(temps)
        average = sum(temps) / len(temps)
        return {"minimum": minimum, "maximum": maximum, "average": average}
    
    
# Main loop to collect temperatures from the user
while(True):
    temp = input("Enter the temperature ('done' to stop): ")
    
    if temp == "done":
        break
    else:
        temperatures.append(float(temp))
        

# Printing the summary of the temperatures
print(summarize(temperatures))
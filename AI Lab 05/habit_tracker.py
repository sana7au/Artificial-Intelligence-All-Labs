# Initial List of Tuples
habits = [("Drink water", True), ("Read 10 pages", False), 
("Exercise", True), ("Sleep 8 hours", True), ("Meditate", False), ("Write journal", True)] 

# Loop through the list to print each habit with its status
for habit in habits:
    print(f"{habit[0]}: {'Done' if habit[1] else 'Not done'}")
    
# Function to generate habit report 
def habit_report(habits):
    completed_count = 0
    for habit in habits:
        if habit[1] == True:
            completed_count += 1
    return {"completed": completed_count, "total": len(habits)}

# Printing the report
print(habit_report(habits))
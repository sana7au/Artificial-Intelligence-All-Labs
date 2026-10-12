attendance = ["Present", "Present", "Absent", "Present", "Absent",
              "Present", "Present", "Absent", "Present", "Present"]

for attend in attendance:
    print(attend, " ")
    
present = 0
absent = 0
total = len(attendance)
    
for i in range(total):
    if attendance[i] == "Present":
        present += 1
    else:
        absent += 1
        
print("\nPresent: ", present)
print("Absent: ", absent)

print("\nFirst 5 attendance: ", attendance[:5])
print("Last 5 attendance: ", attendance[-5:])

attendance.reverse()

print("\nReversed attendance: ", attendance)

print("\nAttendance percentage: ", (present / total) * 100, "%")
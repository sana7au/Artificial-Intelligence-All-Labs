names = ["Ali", "Sara", "Bilal", "Ayesha", "Hamza", "Zain"]

print("Original List: ", names)

print("\nPositive Indexing:")
print("First Student: ", names[0])
print("Last Student: ", names[5])

print("\nNegative Indexing:")
print("First Student: ", names[-6])
print("Last Student: ", names[-1])

names.append("Usman")
print("\nList after appending a new student: ", names)

names.insert(2, "Noor")
print("\nList after inserting a new student at position 2: ", names)

names.remove("Ayesha")
print("\nList after removing a student by name: ", names)

print("\nFinal List: ", names)

print("\nTotal Students: ", len(names))
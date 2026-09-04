students = {
    101: ("Tony", "ENTC", 99),
    102: ("Steve", "MECH", 75),
    103: ("Bruce", "CSE", 95)
}
roll_no = [101, 102, 103]

# Add a new record
students[104] = ("Natasha", "IT", 85)
roll_no.append(104)

# Delete a record
del students[102]
roll_no.remove(102)

# Update an existing record
students[103] = ("Bruce", "AIML", 94)

# Print the updated records with corrected loop variable name and proper indentation
print("Updated Record of Students:")
for roll, i in students.items():
    print("Roll Number: ", roll)
    print("Name: ", i[0])
    print("Branch: ", i[1])
    print("Marks: ", i[2])
    print()

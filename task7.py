
# Student Timetable Conflict Detection

# Course schedules represented as tuples:
# (course_name, day, start_time, end_time, room)

courses = [
    ("Python", "Monday", 9, 11, "R101"),
    ("Mathematics", "Monday", 10, 12, "R102"),
    ("Physics", "Tuesday", 9, 10, "R103"),
    ("Chemistry", "Monday", 11, 12, "R101")
]

# Unavailable rooms represented as a set
unavailable_rooms = {"R103", "R105"}

# Schedule represented as strings
print("COURSE SCHEDULES")
for course in courses:
    schedule = (
        f"{course[0]}: {course[1]}, "
        f"{course[2]}:00-{course[3]}:00, Room {course[4]}"
    )
    print(schedule)

conflicts = []
room_issues = []

# Check unavailable rooms
for course in courses:
    if course[4] in unavailable_rooms:
        room_issues.append(course)

# Detect overlapping periods on the same day
for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1 = courses[i]
        c2 = courses[j]

        if c1[1] == c2[1]:
            if c1[2] < c2[3] and c2[2] < c1[3]:
                conflicts.append((c1, c2))

# Display time conflicts
print("\nTIME CONFLICTS")
if conflicts:
    for c1, c2 in conflicts:
        print(c1[0], "overlaps with", c2[0],
              "on", c1[1])
else:
    print("No time conflicts found.")

# Display unavailable room issues
print("\nUNAVAILABLE ROOM ISSUES")
if room_issues:
    for course in room_issues:
        print(course[0], "uses unavailable room", course[4])
else:
    print("No room issues found.")

# Validate proposed timetable
print("\nTIMETABLE VALIDATION")
if not conflicts and not room_issues:
    print("Timetable is valid.")
else:
    print("Timetable is invalid. Please resolve the issues.")

print("\nTotal time conflicts:", len(conflicts))
print("Total room issues:", len(room_issues))

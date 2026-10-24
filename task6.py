
# University Admission Decision Engine

applicants = []

n = int(input("Enter number of applicants: "))

aggregate_cutoff = float(input("Enter minimum aggregate marks: "))
maths_cutoff = float(input("Enter minimum Maths marks: "))
physics_cutoff = float(input("Enter minimum Physics marks: "))
course_cutoff = float(input("Enter course-specific cutoff: "))

for i in range(n):
    print("\nEnter details for applicant", i + 1)

    name = input("Enter applicant name: ")
    maths = float(input("Enter Maths marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    aggregate = float(input("Enter aggregate percentage: "))
    course_marks = float(input("Enter course-specific marks: "))

    # Check subject eligibility and marks
    if (maths >= maths_cutoff and
        physics >= physics_cutoff and
        aggregate >= aggregate_cutoff and
        course_marks >= course_cutoff):

        applicants.append({
            "name": name,
            "aggregate": aggregate,
            "maths": maths,
            "physics": physics,
            "course_marks": course_marks
        })

# Rank eligible applicants
# Tie-breaking criteria:
# 1. Higher aggregate
# 2. Higher Maths marks
# 3. Higher Physics marks
applicants.sort(
    key=lambda x: (
        x["aggregate"],
        x["maths"],
        x["physics"]
    ),
    reverse=True
)

# Display ranked list
print("\n===== UNIVERSITY ADMISSION RESULTS =====")

if len(applicants) == 0:
    print("No eligible applicants found.")
else:
    print("Rank\tName\t\tAggregate\tMaths\tPhysics")

    for rank, applicant in enumerate(applicants, start=1):
        print(
            rank, "\t",
            applicant["name"], "\t\t",
            applicant["aggregate"], "\t\t",
            applicant["maths"], "\t",
            applicant["physics"]
        )

print("\nTotal eligible applicants:", len(applicants))
print("Total rejected applicants:", n - len(applicants))

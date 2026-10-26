@@ -0,0 +1,75 @@


NUM_SUBJECTS = 3

students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88]
]


def sum_scores(student):
    """Return the total of numeric scores in a student record, skipping the name."""
    total = 0
    for score in student[1:]:
        total = total + score
    return total


def average_score(student):
    return sum_scores(student) / NUM_SUBJECTS


def count_above_avg(records):
    class_total = 0
    for student in records:
        class_total = class_total + average_score(student)
    class_average = class_total / len(records)
    count = 0
    for student in records:
        if average_score(student) > class_average:
            count = count + 1
    return count


print("REPORT")

for student in students:
    total = sum_scores(student)
    average = average_score(student)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{student[0]}{total}{average}{grade}")

class_total = 0

for student in students:
    class_total = class_total + average_score(student)

print(f"Class average:{class_total / len(students)}")
print(f"Above average:{count_above_avg(students)}")

highest_average = 0
topper_name = ""

for student in students:
    average = average_score(student)

    if average > highest_average:
        highest_average = average
        topper_name = student[0]

print(f"Topper:{topper_name}{highest_average}")

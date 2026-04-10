import csv
import os

import csv
import os

def save_student(student, percent, grade):
    file_exists = os.path.isfile("students.csv")

    with open("students.csv", "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "Roll", "Name", "Class",
                "Maths", "Physics", "Chemistry",
                "Percentage", "Grade"
            ])

        writer.writerow([
            student.roll,
            student.name,
            student.class_name,
            student.marks["Maths"],
            student.marks["Physics"],
            student.marks["Chemistry"],
            percent,
            grade
        ])


import csv

def find_by_roll(roll):
    with open("students.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if row and row[0] == roll:
                return row

    return None

import csv

def delete_by_roll(roll):
    rows = []

    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] != roll:
                rows.append(row)

    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

import csv

def update_by_roll(roll, new_data):
    rows = []

    with open("students.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if row and row[0] == roll:
                rows.append(new_data)
            else:
                rows.append(row)

    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

import csv

def fetch_all_reports():
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        return list(reader)
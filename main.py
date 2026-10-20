import pandas as pd
import numpy as np

data = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": [
        "Priyanka", "Reshma", "Jahnavi", "Susmitha", "Yamuna", "JayaSree","Reena", "Nithin", "Gagan", "Punith"
    ],
    "HTML"      : [85,60,88,98,95,65,86,45,87,83],
    "CSS"       : [78,92,65,85,96,98,89,76,54,35],
    "JAVASCRIPT": [90,75,88,97,95,73,55,73,81,39],
    "SQL"       : [76,70,97,99,87,78,97,58,97,76],
    "PYTHON"    : [82,78,70,88,79,77,98,34,54,45],
    "Attendance": [92,85,98,75,94,88,96,85,74,86]
}

pd.DataFrame(data).to_csv("student_data.csv", index=False)
df = pd.read_csv("student_data.csv")

print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
print("\nSTUDENT DATA")
print(df.to_string(index=False))

subjects = ["HTML", "CSS", "JAVASCRIPT", "SQL", "PYTHON"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = np.round(df[subjects].mean(axis=1), 2)
def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"

df["Grade"] = df["Average"].apply(calculate_grade)
df["Result"] = df[subjects].min(axis=1).apply(
    lambda mark: "Pass" if mark >= 35 else "Fail"
)
print("\nSTUDENT PERFORMANCE REPORT")
print(df[[
    "Student_ID", "Name", "Total",
    "Average", "Grade", "Result"
]].to_string(index=False))
print("\nCLASS ANALYSIS")
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())
df.to_csv("student_performance.csv", index=False)

print("\nCSV files created successfully......")
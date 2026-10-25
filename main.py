import pandas as pd
import numpy as np

data = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": [
        "Anusha", "Sriya", "Sujitha", "Sandhya", "Ramya", "Mounika","Hema", "Shalini", "Jyoshika", "pavani"
    ],
    "HTML"      : [87,98,67,95,87,94,69,88,72,87],
    "CSS"       : [87,98,67,74,82,99,76,87,66,58],
    "JAVASCRIPT": [89,76,68,65,73,94,32,98,88,87],
    "SQL"       : [85,98,84,65,88,87,94,97,66,97],
    "PYTHON"    : [78,70,88,34,54,77,85,99,76,45],
    "Attendance": [92,85,98,99,67,83,97,55,74,86]
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
# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python program that processes marks for 10 students in HTML, CSS, JavaScript, SQL, and Python. It calculates each student's total and average, assigns a grade, determines pass/fail status, summarizes class performance, and saves the processed data to a CSV file.

## Objectives
- Store and read student marks and attendance using a CSV file.
- Calculate each student's total and average across five subjects.
- Assign a grade based on the calculated average.
- Determine pass/fail status using the minimum mark across the five subjects.
- Summarize class performance and export the processed report.

## Technologies Used
- **Python** — main programming language.
- **Pandas** — creates, reads, processes, and exports tabular data.
- **NumPy** — rounds average marks to two decimal places.
- **CSV** — stores the input data and generated performance report.

## Project Files
- `main.py` — Python source code.
- `student_data.csv` — original student marks and attendance; created by the program.
- `student_performance.csv` — processed output containing the original fields plus Total, Average, Grade, and Result.
- `README.md` — project description and instructions.

## Grade and Result Rules
| Average | Grade |
|---|---|
| 90 and above | S |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| Below 60 | F |

A student is marked **Pass** if the minimum mark across HTML, CSS, JavaScript, SQL, and Python is at least 35. Otherwise, the result is **Fail**. Attendance is included in the dataset but is not used to calculate grades or pass/fail results.

## Input Dataset
The program contains 10 student records. Each record includes Student ID, Name, marks in HTML, CSS, JavaScript, SQL, and Python, and Attendance.

## Implementation
1. Import Pandas and NumPy.
2. Define the student IDs, names, marks, and attendance in a dictionary.
3. Write the input data to `student_data.csv` and read it into a DataFrame.
4. Display the original student data.
5. Calculate each student's total and average for the five subjects.
6. Assign grades using the grading rules.
7. Determine Pass or Fail from the minimum mark across the five subjects.
8. Print the student performance report and class analysis.
9. Save the processed DataFrame to `student_performance.csv`.

## How to Run in VS Code
1. Install Python and the Microsoft Python extension in VS Code.
2. Open the folder containing `main.py`.
3. Open **Terminal → New Terminal**.
4. Install the required libraries if needed:
   ```bash
   python -m pip install pandas numpy
   ```
5. Run the program:
   ```bash
   python main.py
   ```
6. Check the terminal for the student report and class analysis. The program creates `student_data.csv` and `student_performance.csv` in the current working folder.

## Program Output
For the dataset in the supplied code, the class average is **79.50**, the highest average is **93.80** (Shalini), the lowest average is **66.60** (Sandhya), and **8 students pass while 2 students fail**, based on the program's current pass/fail rule.

## Final Outcome
The program generates a structured student-wise performance report and class-level summary. It also saves the original and processed student data as CSV files, making the results easier to review.

## Important Note About the Supplied Code
The uploaded `main.py` needs a comma after the HTML marks list, before the CSS entry, in the `data` dictionary. Add this comma before running the program; otherwise, Python will report a syntax error.

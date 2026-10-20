# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python program that processes student marks in HTML, CSS, JavaScript, SQL, and Python. It calculates totals and averages, assigns grades, determines pass/fail results, summarizes class performance, and saves the processed report to a CSV file.

## Objectives
- Store and read student marks using CSV files.
- Calculate each student's total and average across five subjects.
- Assign a grade based on the calculated average.
- Determine pass/fail status using the minimum mark across the five subjects.
- Summarize class performance and export the processed report.

## Technologies Used
- **Python** — main programming language.
- **Pandas** — creates, reads, processes, and exports tabular data.
- **NumPy** — calculates averages and rounds them to two decimal places.
- **CSV** — stores input data and the generated performance report.

## Project Files
- `main.py` — Python source code.
- `student_data.csv` — input student marks and attendance. The program creates this file from the data defined in the source code.
- `student_performance.csv` — output file containing marks plus Total, Average, Grade, and Result.
- `README.md` — project description and run instructions.

## Grade and Result Rules
| Average | Grade |
|---|---|
| 90 and above | S |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| Below 40 | F |

A student is marked **Pass** if the lowest mark across HTML, CSS, JavaScript, SQL, and Python is at least 35; otherwise, the result is **Fail**. Attendance is included in the data but is not used in the grade or pass/fail calculation.

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
6. Check the terminal for the student report and class analysis. The program writes `student_data.csv` and `student_performance.csv` in the current working folder.

## Implementation
1. Imports Pandas and NumPy.
2. Defines student IDs, names, marks, and attendance.
3. Writes the input data to `student_data.csv` and reads it back into a DataFrame.
4. Calculates each student's total and average for the five subjects.
5. Applies the grading function and pass/fail rule.
6. Prints the detailed report and class statistics.
7. Saves the processed DataFrame to `student_performance.csv`.

## Final Outcome
The program generates a structured student performance report and class-level summary. In the supplied dataset, the class average is **77.32**, the highest average is **93.40** (Susmitha), the lowest average is **55.60** (Punith), and **9 students pass while 1 student fails** under the program's current rule.

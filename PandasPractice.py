import pandas as pd
# Pandas practice Task
data = {
    "Name": ['Gai', 'Kai', 'Wal', 'Koang'],
    "Age": [23, 25, 21, 30],
    "Grade": [45, 75, 88, 30]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Adding column "Passed"
df["Passed"] = df["Grade"] > 50
print("\nDataframe with 'Passed' column:\n", df)

# Filter only students who passed
passed_students = df[df["Passed"] == True]
print("\nStudents who passed:\n", passed_students)
print(passed_students[["Name", "Age"]])

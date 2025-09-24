# Importing math library
import pandas as pd
import numpy as np
import datetime
import random
import math
print(math.sqrt(16))
print(math.pi)
print("Square root of 36:", math.sqrt(36))
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print("Power of 2^3:", math.pow(2, 3))

# importing random library
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

# Importing datetime library
today = datetime.date.today()
print("Today's date is:", today)
now = datetime.datetime.now()
print("Current date and time is:", now)
print("Current time:", now.strftime("%H:%M:%S"))

# Importing numpy library
# Array creation
my_array = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", my_array)

# Array operations
print("Array multiplied by 2:", my_array * 2)
print("Array mean:", np.mean(my_array))
print("Mean:", np.mean(my_array)
      )
print("Square Roots:", np.sqrt(my_array))

# Numpy practice Task
arr = np.arange(10, 51)
print("Array from 10 to 50:", arr)
# Find the maximum and minimum values
print("Maximum value:", arr.max())
print("Minimum value:", arr.min())

# Multiply each element by 3
arr_multiplied = arr * 3
print("Array elements multiplied by 3:", arr_multiplied)

# Importing pandas library
# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Score': [85, 90, 78, 92]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
# Displaying basic information about the DataFrame
print("DataFrame Info:")
print("Names:", df['Name'])

# Filtering rows.
print("Scores above 90:")
print(df[df['Score'] > 90])

# Pandas practice Task
data = {
    "Name": ['Gai', 'Kai', 'Wal', 'Koang'],
    "Age": [23, 25, 21, 30],
    "Grade": ['A', 'B', 'A', 'C']
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

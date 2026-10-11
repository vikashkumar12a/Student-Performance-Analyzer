import pandas as pd 
import numpy as np 
n = int(input("Enter numbers of students: "))
data = []
for i in range(n):
    print(f"\nStudent {i+1}")

    name = input("Enter student name: ")
    python_marks = int(input("Enter Python marks: "))
    pandas_marks = int(input("Enter Pandas marks: "))
    numpy_marks = int(input("Enter numpy marks: "))
    dsa_marks = int(input("Enter dsa marks: "))
    maths_marks = int(input("Enter maths marks: "))

    data.append({
        "Name": name,
        "Python": python_marks,
        "Pandas": pandas_marks,
        "NumPy": numpy_marks,
        "DSA": dsa_marks,
        "Maths": maths_marks
    })

df = pd.DataFrame(data)
subjects = ["Python", "Pandas", "NumPy", "DSA", "Maths"]
print(df)

df["Total"] =df["Python"] + df["Pandas"] + df["NumPy"] + df["DSA"] + df["Maths"]
df["Average"] = df[["Python", "Pandas", "NumPy", "DSA", "Maths"]].mean(axis=1)
df["Highest"] = df[subjects].max(axis=1)
df["Lowest"] = df[subjects].min(axis=1)
df["Result"] = np.where((df[subjects] < 35).any(axis=1), "Fail", "Pass")

print(df)
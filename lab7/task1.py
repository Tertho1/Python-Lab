import pandas as pd

data = {
    "StudentID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", 
             "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Math": [85, 90, 78, 92, 88, 80, 95, 87, 76, 89],
    "Algorithm": [80, 75, 88, 90, 85, 70, 78, 92, 88, 83],
    "Programming": [78, 85, 92, 88, 75, 90, 80, 85, 95, 77]
}

df = pd.DataFrame(data)
print("DataFrame Overview:\n", df)

print("\nDescriptive Statistics:\n", df.describe())

subject_columns = ["Math", "Algorithm", "Programming"]

avg_scores = df[subject_columns].mean()
print("\nAverage Score for each Subject:\n", avg_scores)

max_scores = df[subject_columns].max()
print("\nHighest Score for each Subject:\n", max_scores)

min_scores = df[subject_columns].min()
print("\nLowest Score for each Subject:\n", min_scores)

def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

for subject in subject_columns:
    df[f'{subject}_Grade'] = df[subject].apply(determine_grade)

a_counts = {subject: df[f'{subject}_Grade'].value_counts().get('A', 0) for subject in subject_columns}
print("\nNumber of students who got an A in each subject:\n", a_counts)

df['Average_Score'] = df[subject_columns].mean(axis=1)
print("\nAverage Score for each Student:\n", df[['StudentID', 'Name', 'Average_Score']])

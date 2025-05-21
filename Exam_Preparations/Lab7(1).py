import pandas as pd

data={
    "ID":[11,17,16,8,37,18,6,24,19,20],
    "Name": ["Tertho", "Sweety", "Antor", "Eleas","Ratul","Topu","Rima","Rupa","Shanta","Sabikun"],
    "Math": [98, 92, 78, 90, 88, 95, 80, 85, 80, 95],
    "Programming": [96, 95, 80, 85, 90, 92, 85, 88, 90, 95],
    "Algorithm": [97, 85, 88, 92, 95, 90, 85, 88, 92, 95],
}

df=pd.DataFrame(data)
print(f"Average Number in Math : {df["Math"].mean()}")
print(f"Average Number in Programming : {df["Programming"].mean()}")
print(f"Average Number in Algorithm : {df["Algorithm"].mean()}")
print(f"Highest Score : {df[['Math', 'Programming', 'Algorithm']].max()}")
print(f"Lowest Score :\n{df[['Math', 'Programming', 'Algorithm']].min()}")

def getgrades(score):
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

for subject in ["Math","Programming","Algorithm"]:
    df[f"{subject}_Grade"]=df[subject].apply(getgrades)
print(df)

for grade in ["Math_Grade","Programming_Grade","Algorithm_Grade"]:
    grade_counts = df[grade].value_counts().get('A',0)
    print(f"Number of students with A in {grade} : {grade_counts}")
        

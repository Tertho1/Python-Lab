import numpy as np

grades = np.array([
    [85, 90, 78], 
    [88, 76, 92], 
    [90, 85, 88], 
    [75, 80, 85], 
    [95, 92, 90]  
])

total_grades = np.sum(grades, axis=1)
average_per_subject = np.mean(grades, axis=0)
highest_per_subject = np.max(grades, axis=0)

print("Total grades per student:", total_grades)
print("Average grade per subject:", average_per_subject)
print("Highest grade per subject:", highest_per_subject)

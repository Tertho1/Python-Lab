import numpy as np
grades=np.array(
    [[84,92,87],[92,95,83],[88,83,89],[92,78,81],[85,94,82]]
)
total_grades_per_subject=np.sum(grades,axis=0)
total_grades_per_student=np.sum(grades,axis=1)
print(f"Total grades per subject: {total_grades_per_subject}")
print(f"Total grades per student: {total_grades_per_student}")
highest_per_subject=np.max(grades,axis=0)
print(f"Highest grade per subject: {highest_per_subject}")

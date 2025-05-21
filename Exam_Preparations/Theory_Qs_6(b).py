try:
    with open("Exam_Preparations/marks.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 4:
                print("Wrong number of values in line:", line)
                continue
            name = parts[0]
            try:
                marks = [float(x) for x in parts[1:]]
            except ValueError:
                print(f"Non-numeric value in line: {line}")
                continue
            if any(mark < 0 for mark in marks):
                print(f"Negative value in line: {line}")
                continue
            average = sum(marks) / len(marks)
            print(f"Name: {name}, Average: {average:.2f}")
            if average >= 90:
                grade = "Excellent"
            elif average >= 70:
                grade = "Good"
            else:
                grade = "Average"
            print(f"Grade : {grade}")
except FileNotFoundError:
    print("File was not found")
except Exception as e:
    print(e)

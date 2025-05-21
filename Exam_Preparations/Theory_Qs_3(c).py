with open("input.txt", "r") as file:
    line=file.read().strip()
    
line=line.replace("dogs","cats")
with open("output.txt", "w") as file:
    file.write(line)
employees=["Tertho","Antor","Asash"]
service_years=[4,7,3]

def get_experience_level(year):
    if year <=2:
        return "Junior"
    elif year<=5:
        return "Mid Level"
    elif year<=9:
        return "Senior"
    else:
        return "Expert"
for name,year in zip(employees,service_years):
    print(f"{name} has {year} years of service and is a {get_experience_level(year)} employee.")    
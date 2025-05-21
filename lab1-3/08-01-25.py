def func():
    dict = {"Tertho": 11, "Antor": 16}
    dict2={1: "Tertho", 2: "Antor", 5: "Tahmid"}
    print(dict)
    print(dict["Tertho"])
    for i in dict:
        print(i,dict[i])
    for i in dict2:
        print(dict2[i],i)


func()

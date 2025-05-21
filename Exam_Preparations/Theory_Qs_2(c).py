dict={"Asfi":70000,
      "Ali":80000,
      }
dict["Ratan"]=75000
dict["Ali"]=85000
del dict["Asfi"]
for key,value in dict.items():
    print(key,value)
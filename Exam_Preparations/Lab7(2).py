import pandas as pd

df=pd.read_csv("FuelConsumptionCo2.csv")

# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.info())
# print(df.mean(numeric_only=True))
# print(df.median(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True)) 
# print(df.sum(numeric_only=True))
# print(df.count()) 
# print(df.std(numeric_only=True))
# print(df.var(numeric_only=True))
# print(df.fillna(0))
# print(df.dropna(how="all"))
# print(df.dropna(how="any"))
# print(df.dropna(axis=1))
# print(df.dropna(axis=0))
# print(df.sort_values(by="MAKE", ascending=True))
# print(df.groupby("MAKE")[["FUELCONSUMPTION_CITY","FUELCONSUMPTION_HWY"]].mean())
# print(df.groupby("MAKE")[["FUELCONSUMPTION_CITY","FUELCONSUMPTION_HWY"]].agg(["mean","sum"]))
# pt=pd.pivot_table(df,index=["MAKE"],values=["FUELCONSUMPTION_CITY","FUELCONSUMPTION_HWY"],aggfunc=["mean","sum"])
# print(pt)
# df['CO2EMISSIONS']=df['CO2EMISSIONS'].apply(lambda x: x/1000)
# print(df['CO2EMISSIONS'])

import pandas as pd
data = pd.read_csv("data.csv")
print("EV CHARGING DATA")
print(data)
total_units=data["Units_Consumed"].sum()
average_units=data["Units_Consumed"].mean()
highest_day=data.loc[data["Units_Consumed"].idxmax(),"Day"]
total_cost=data["Cost"].sum()
print("\nEV CHARGING ANALYSIS RESULT")
print("Total Units Consumed:",total_units)
print("Average Units Consumed:",round(average_units,2))
print("Highest Consumption day:",highest_day)
print("Total Charging cost:",total_cost)
if average_units > 12:
    print("\nSuggestion:Charging during night hours can improve energy efficiency.")
else:
    print("\nSuggestion:Current charging pattern is efficient.")

import pandas as pd

WeightKg= 0
HeightCm = 0

data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

#data
Final = pd.DataFrame(data)
Final

Final['Height_m']=(Final['HeightCm']/100)
Final['Height_m']
Final['BMI'] =Final['WeightKg'] / Final['Height_m'].pow(2)

print(Final)                   




     



import pandas as pd
import numpy as np

with open('input_day_1.txt') as f:
    lines = f.read()

print(lines)

df = pd.DataFrame([x for x in lines.split('\n')])
df[1] = np.where([x.isnumeric() for x in df[0]], 0, 1)
df[2] = df[1].cumsum()
df[0] = pd.to_numeric(df[0])

calories_sums = df.groupby(2)[0].sum().reset_index()
print(calories_sums)

print(calories_sums[calories_sums[0] == max(calories_sums[0])])
print(df[df[2] == int(calories_sums[calories_sums[0] == max(calories_sums[0])][2])])

calories_sums = calories_sums.sort_values(by = 0, ascending = False).reset_index(drop = True)
top_3_calories = calories_sums.iloc[0:3, ]

print(top_3_calories)
print(top_3_calories[0].sum())


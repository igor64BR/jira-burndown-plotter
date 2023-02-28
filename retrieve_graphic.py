import json
import matplotlib.pyplot as plt
from datetime import datetime
import ast

with open('data.json') as f:
    data = json.load(f)

# prepare data for plotting
x = []
y = {}
for item in data['data']:
    date_str = list(item.keys())[0]
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    x.append(date_obj)
    for status, value in ast.literal_eval(item[date_str]).items():
        if status not in y:
            y[status] = []
        y[status].append(value)

# plot data
plt.figure(figsize=(10, 5))
for status in y:
    plt.plot(x, y[status], label=status)

plt.legend()
plt.show()

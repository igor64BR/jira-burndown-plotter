import json
import matplotlib.pyplot as plt

# Load data from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Extract dates and values
dates = []
values = {}
for item in data['data']:
    for date, value in item.items():
        dates.append(date)
        value_dict = json.loads(value)
        for k in ['To Do', 'Done', 'In Progress', 'HOLD']:
            if k not in values:
                values[k] = []
            values[k].append(value_dict.get(k, 0))

# Plot line graph
for k, v in values.items():
    plt.plot(dates, v, label=k)

plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()

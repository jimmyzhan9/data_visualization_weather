import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "venv/death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax.set_title("Daily high and low temperatures - Death Valley 2014", fontsize=20)
ax.set_xlabel("Date", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatures(F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()





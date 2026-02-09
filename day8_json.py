import json

week ={
    "Monday": [220],
    "Tuesday": [180, 325],
    "Wednesday": [329],
    "Thursday": [300, 132, 220, 510],
    "Friday": [240]
}

with open("D:\Python Projects\week_earnings.json", "w") as file:
    json.dump(week, file, indent=4)

print("JSON data saved")

import json

with open("D:\Python Projects\week_earnings.json", "r") as file:
    week_loaded = json.load(file)

print(week_loaded)

with open("D:\Python Projects\week_earnings.txt", "r") as file:
    content = file.read()

print(content)

#I added txt file to see the different of txt and json file structure

total_week = 0

for day, values in week_loaded.items():
    day_total = sum(values)
    print(day, "total: ", day_total)
    total_week += day_total

print("Total week earnings: ", total_week)

new_day = "Saturday"
new_earnings = [275, 310]

week_loaded[new_day] = new_earnings
with open("D:\Python Projects\week_earnings.json", "w") as file:
    json.dump(week_loaded, file, indent= 4)

print("Updated JSON saved")

best_day = max(
    week_loaded,
    key=lambda day: sum(week_loaded[day])
)

print("Best performing day: ", best_day)
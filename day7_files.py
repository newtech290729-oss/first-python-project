file = open("D:\Python Projects\earnings.txt", "w")

file.write("Monday: 220\n")
file.write("Tuesday: 325\n")
file.write("Wednesday: 329\n")

file.close()

print("Data Saved")

file = open("D:\Python Projects\earnings.txt", "r")

content = file.read()
print(content)

file.close()

with open("D:\Python Projects\earnings.txt", "a") as file:
    file.write("Thursday: 300\n")
    file.write("Friday: 240\n")

week = {
    "Monday" : [220],
    "Tuesday" : [180, 325],
    "Wednesday" : [329],
    "Thursday" : [300, 132, 229, 510],
    "Friday" : [240]
}

with open("D:\Python Projects\week_earnings.txt", "w") as file:
    for day, values in week.items():
        file.write(f"{day}: {sum(values)}\n")

week_loaded = {}

with open("D:\Python Projects\week_earnings.txt", "r") as file:
    for line in file:
        day, total = line.strip().split(": ")
        week_loaded[day] = float(total)

print(week_loaded)

best_day = max(week_loaded, key=week_loaded.get)
worst_day = min(week_loaded, key=week_loaded.get)

print("Best day: ", best_day)
print("Worst day: ", worst_day)
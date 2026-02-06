earnings = [200, 250, 180, 300, 220]

print(earnings)
print("First day earning:", earnings[0])
print("Total days:", len(earnings))

total = 0

for value in earnings:
    total += value

print("Total earnings: ", total)
print("Average earning: ", round(total/len(earnings), 2))

earnings = []

days = int(input("Enter number of days worked (1-7):"))

for day in range(1, days + 1):
    value = float(input(f"Enter earning for day {day}:"))
    earnings.append(value)

print("\n All earnings:", earnings)
print(earnings)

highest = max(earnings)
lowest = min(earnings)
average = sum(earnings) / len(earnings)

print("Highest earning day: ", highest)
print("Lowest earning day ", lowest)
print("Average earnings: ", round(average, 2))

week = {
    "Monday": 220,
    "Tuesday": 180,
    "Wednesday": 329,
    "Thursday" : 300,
    "Friday": 240
}

print("Wednesday earning: ", week["Wednesday"])

total = 0

for day, earning in week.items():
    print(day, "->", earning)
    total += earning

print("Total: ", total)
print("Average: ", round(total / len(week), 2))

for day, earning in week.items():
    if earning > 280:
        print(day, "was a high performing day")
    elif earning < 200:
        print(day, "was a low-performing day")

week = {
    "Monday": 220,
    "Tuesday": [180, 325],
    "Wednesday": 329,
    "Thursday" : [300, 132, 229, 510],
    "Friday": 240
}

total = 0

for day, earning in week.items():
    print(day, "->", earning)

    if isinstance(earning, list):
        total += sum(earning)
    else:
        total += earning

print("Total earnings: ", total)

week = {
    "Monday": [220],
    "Tuesday": [180, 325],
    "Wednesday": [329],
    "Thursday" : [300, 132, 229, 510],
    "Friday": [240]
}

total = 0

for day, earning in week.items():
    day_total = sum(earning)
    print(day, "->", day_total)
    total += day_total

print("Total earnings: ", total)
def greet():
    print("Welecome to Earnings Analyzer")

greet()
greet()

def print_day_earning(day, amount):
    print(day, "earning: ", amount)

print_day_earning("Monday", 220)
print_day_earning("Tuesday", 325)

def calculate_total(earnings):
    return sum(earnings)

week = {
    "Monday" : [220],
    "Tuesday" : [180,325],
    "Wednesday" : [-329],
    "Thursday" : [-300, -132, -229, 510],
    "Friday" : [240]
}

weekly_total = 0

for day, values in week.items():
    day_total = calculate_total(values)
    print(day, "total: ", day_total)
    weekly_total += day_total

print("Weekly total: ", weekly_total)

def get_day_total(values):
    return sum(values)

def print_performance(day, total):
    if total > 500:
        print(day, "High Performance")
    elif total < 250:
        print(day, "Low performance")
    else:
        print(day, "Normal perfomance")

for day, values in week.items():
    total = get_day_total(values)
    print_performance(day, total)

def validate_earnings(values):
    for v in values:
        if v < 0:
            return False
    return True

for day, values in week.items():
    if not validate_earnings(values):
        print(day, "has invalid data")
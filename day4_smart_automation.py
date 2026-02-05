days_input = input("Enter number of days you worked this week: ")

if not days_input.isdigit():
    print("Error: Days must be a whole number (no decimals, no text).")
    exit()

days = int(days_input)

if days == 0:
    print("Error: Days worked cnanot be zero.")
    exit()

if days < 1 or days > 7:
    print("ERROR: Days worked must be between 1 and 7. ")
    exit()

print("Days", days)

total_earnings = 0.0

for day in range(1, days +1):
    earning_input = input(f"Enter earnings for day {day}: ")

    try:
        earning = float(earning_input)
    except ValueError:
        print("ERROR: Earnings must be a number:")
        exit()

    total_earnings += earning
    print("Total", total_earnings)

    average = total_earnings / days

print("\n==== WEEKLY SUMMARY====")
print("Total Earnings: ", round(total_earnings, 2))
print("Average per day: ", round(average, 2))

if average < 150:
    print("⚠️Alert: Earnings are below expected level.")
elif average > 300:
    print("🔥Great job! High earning week.")
else:
    print("👍Earnings are in normal range.")
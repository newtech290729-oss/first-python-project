#for i in range(5):
#    print("This is repetition number", i + 1)

#counter = 0

#while counter < 5:
#    print("Counter is at ", counter)
#    counter += 1.2


days = int(input("Enter number of days you worked this week: "))

#if not days.isdigit():
#    print("Error: Number of days must be a whole number. No decimals allowed")
#else:
#    days = days
    
total_earning =0.0

for day in range(days):
#    earnings = float(input(f"Enter your earnings for day {day +1}: "))
    earnings = float(input("Enter your earnings for day " + str(day +1) + ": "))
    total_earning += earnings

print("Your total earnings for ", days, " days is: ", total_earning)
print("Average daily earning:", total_earning / days)
print("Average daily earning:", round(total_earning / days, 3))
print("Your total earnings for ", days, "days is:", round(total_earning, 2))
print("Average daily earning: ", round(total_earning / days, 2))


# Get valid number of days
while True:
    user_input = input("Enter number of days you worked this week: ")

    if user_input.isdigit():
        days = int(user_input)
        break
    else:
        print("❌ Enter a whole number only (no decimals).")

total_earning = 0.0

for day in range(days):
    earnings = float(input(f"Enter your earnings for day {day + 1}: "))
    total_earning += earnings

print("Total earnings:", round(total_earning, 2))
print("Average daily earning:", round(total_earning / days, 2))

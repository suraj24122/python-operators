# Write a program to convert minutes into hours and minutes. (e.g., 150 minutes = 2 hours 30 minutes)

# 1. Get the number of minutes from the user.
minutes = int(input("Enter the number of minutes: "))

# 2. Calculate hours and remaining minutes.
hours = minutes // 60
remaining_minutes = minutes % 60

# 3. Print the result.
print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")

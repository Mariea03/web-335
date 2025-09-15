"""
Author: Nies
Date: 09/13/2025
File Name: nies_lemonadeStandSchedule.py
Description: This program prints out a lemonade stand task list and schedules 
tasks for each day of the week, using for loops and conditional statements.
"""

tasks = [
    "Buy lemons and sugar",
    "Make lemonade",
    "Set up the stand",
    "Sell lemonade to customers",
    "Count earnings and clean up"
]

print("Lemonade Stand Tasks:")
for task in tasks:
    print("-", task)

print("\nWeekly Schedule:")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(len(days)):
    day = days[i]

    if day == "Saturday" or day == "Sunday":
        print(f"{day}: Day off! Get some rest.")
    else:
        task = tasks[i % len(tasks)]
        print(f"{day}: {task}")
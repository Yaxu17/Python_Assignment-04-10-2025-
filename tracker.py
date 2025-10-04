# Author: Yokshit Rajora
# Date: 03/10/2025
# Project: Daily Calorie Tracker CLI (Automated Sample Runs)

import datetime

# -----------------------------
# Task 1: Setup & Introduction
# -----------------------------
def run_calorie_tracker(meal_data, daily_limit, save_log=False):
    meals = []
    calories = []

    print("\n Welcome to the Daily Calorie Tracker")
    print("This tool helps you log meals, track calories, and compare against your daily limit.\n")

    # -------------------------------
    # Task 2: Input & Data Collection
    # -------------------------------
    print(f"Logging {len(meal_data)} meals...\n")
    for meal_name, meal_calories in meal_data:
        meals.append(meal_name)
        calories.append(meal_calories)

    print("Meals logged successfully!\n")

    # -----------------------------
    # Task 3: Calorie Calculations
    # -----------------------------
    total_calories = sum(calories)
    average_calories = total_calories / len(calories)

    # -----------------------------------
    # Task 4: Exceed Limit Warning System
    # -----------------------------------
    if total_calories > daily_limit:
        status = " Warning: You exceeded your daily calorie limit!"
    else:
        status = " Great! You are within your daily calorie limit."

    # -------------------------------
    # Task 5: Neatly Formatted Output
    # -------------------------------
    print("Daily Calorie Summary")
    print(f"{'Meal Name'.ljust(20)}{'Calories'}")
    print("-" * 30)
    for i in range(len(meals)):
        print(f"{meals[i].ljust(20)}{calories[i]}")
    print("-" * 30)
    print(f"{'Total:'.ljust(20)}{total_calories}")
    print(f"{'Average:'.ljust(20)}{average_calories:.2f}")
    print(status)

    # ---------------------------------
    # Task 6 (Bonus): Save Session Log
    # ---------------------------------
    if save_log:
        try:
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            filename = r"C:\Users\yoksh\OneDrive\Documents\College\Subjects\Python\Assignments\daily_calorie_tracker\calorie_log.txt"

            with open(filename, "a+") as file:
                file.write("\n Daily Calorie Tracker Log \n")
                file.write(f"Date & Time: {timestamp}\n\n")
                file.write(f"{'Meal Name'.ljust(20)}{'Calories'}\n")
                file.write("-" * 30 + "\n")
                for i in range(len(meals)):
                    file.write(f"{meals[i].ljust(20)}{calories[i]}\n")
                file.write("-" * 30 + "\n")
                file.write(f"{'Total:'.ljust(20)}{total_calories}\n")
                file.write(f"{'Average:'.ljust(20)}{average_calories:.2f}\n")
                file.write(status + "\n")

            print(f"\n Session saved to {filename} successfully!")
        except Exception as e:
            print(f" Error saving session: {e}")
    else:
        print("Session not saved.")

# ---------------------
# Run 4 Sample Sessions
# ---------------------
sample_sessions = [
    {
        "meal_data": [("Breakfast", 350), ("Lunch", 600), ("Dinner", 500)],
        "daily_limit": 1600,
        "save_log": True
    },
    {
        "meal_data": [("Smoothie", 200), ("Salad", 300), ("Roll", 450)],
        "daily_limit": 1200,
        "save_log": False
    },
    {
        "meal_data": [("Paratha", 400), ("Dal Chawal", 550), ("Sambar", 300)],
        "daily_limit": 1400,
        "save_log": True
    },
    {
        "meal_data": [("Chole bhature", 600), ("Saag", 800), ("Dal Roti", 200)],
        "daily_limit": 1400,
        "save_log": True
    }
]

for i, session in enumerate(sample_sessions, start=1):
    print(f"\n\n Running Sample Session {i} ")
    run_calorie_tracker(**session)
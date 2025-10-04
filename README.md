# 🍎 Daily Calorie Tracker CLI

**Author:** Yokshit Rajora  
**Date:** 03/10/2025  
**Project:** Daily Calorie Tracker CLI (Automated Sample Runs)  

---

# 📖 Project Overview

The **Daily Calorie Tracker** is a Python-based Command-Line Interface (CLI) tool that allows users to:

- Log meals and their respective calorie values.  
- Track total and average calorie intake for the day.  
- Compare intake against a user-defined daily calorie limit.  
- Receive alerts if the calorie limit is exceeded.  
- Optionally save session logs to a text file for future reference.  

This project demonstrates Python concepts such as **lists, loops, functions, file handling, and formatted output**.

---

# 🛠 Features

1. **Meal Logging** – Enter multiple meals along with calories consumed.  
2. **Automatic Calculations** – Calculates total and average calories.  
3. **Exceed Limit Warning** – Alerts when daily limit is exceeded.  
4. **Formatted Summary** – Displays meals, calories, total, and average neatly in the terminal.  
5. **Session Log Saving** – Optionally saves session logs with timestamp to a text file.  

---

# ⚡ Usage

1. Clone or download the repository.  
2. Open the Python script `daily_calorie_tracker.py`.  
3. Define your meal data, daily calorie limit, and whether to save the log.  
4. Run the script in a Python 3 environment.  
5. View summary and optional log file output.  

# -> Example

meal_data = [("Breakfast", 350), ("Lunch", 600), ("Dinner", 500)]
daily_limit = 1600
save_log = True

run_calorie_tracker(meal_data, daily_limit, save_log)

# 💡 Sample Output

📊 Daily Calorie Summary 📊
Meal Name           Calories
------------------------------
Breakfast           350
Lunch               600
Dinner              500
------------------------------
Total:              1450
Average:            483.33
✅ Great! You are within your daily calorie limit.

If saving is enabled, the session is appended to:
C:\Users\yoksh\OneDrive\Documents\College\Subjects\Python\Assignments\daily_calorie_tracker\calorie_log.txt

# 🎓 Resources & References

This project was guided by educational platforms:

-> YouTube Channels:
>> Bro Code => https://www.youtube.com/@BroCode
>> Apnacollege => https://www.youtube.com/@Apnacollege

-> Web Tutorials:
>> W3Schools Python Tutorials => https://www.w3schools.com/python/

These resources helped in learning Python functions, loops, file handling, and formatted output.

# 📌 Notes

1.Log file location can be changed as per your system.
2.Ensure your daily calorie limit is realistic and personalized.
3.This tool is intended for educational purposes and basic tracking, not professional dietary advice.
import datetime

def track_habit(habit_name, num_days=7):
    print(f"--- Tracking Habit: {habit_name} ---")
    completion_history = []
    today = datetime.date.today()

    print(f"Simulating tracking for the last {num_days} days...")
    for i in range(num_days):
        current_date = today - datetime.timedelta(days=num_days - 1 - i)
        response = input(f"Did you complete '{habit_name}' on {current_date.strftime('%Y-%m-%d')}? (y/n): ").lower()
        completed = response == 'y'
        completion_history.append(completed)
        print(f"  -> Recorded: {'Completed' if completed else 'Missed'}")

    print("\n--- Habit Tracking Summary ---")
    print(f"Habit: {habit_name}")
    print(f"History: {[('✅' if c else '❌') for c in completion_history]}")

    # --- AI-powered Insight/Recommendation (Simplified) ---
    # This section simulates the "AI-powered" aspect mentioned in the article.
    # It provides tailored feedback based on simple rules derived from tracking data,
    # mimicking how an intelligent system might offer personalized guidance.

    total_completed = sum(1 for c in completion_history if c)
    completion_rate = (total_completed / num_days) * 100

    print(f"\n--- AI-Powered Insight for '{habit_name}' ---")
    print(f"Overall Completion Rate: {completion_rate:.1f}%")

    if completion_rate >= 80:
        print("Fantastic work! You've consistently completed this habit. Consider increasing the challenge or adding a new related habit to build on this success!")
    elif completion_rate >= 50:
        print("Good progress! You're building momentum. Try to identify any specific hurdles on days you missed and plan around them.")
        if not completion_history[-1]: # Missed last day
            print("  Tip: Don't let one miss derail you. Get back on track today!")
    else:
        print("It looks like you're finding this habit challenging. Don't worry, that's normal!")
        print("  Recommendation: Let's try simplifying the habit or breaking it into smaller, easier steps. For example, instead of 'Exercise for 30 min', try 'Exercise for 5 min'.")
        if completion_history.count(False) >= 2 and completion_history[-2:] == [False, False]: # Missed last two days
             print("  Urgent Tip: You've missed the last two days. Re-evaluate why and make a plan for tomorrow. Consistency is key!")
        elif completion_history.count(False) >= 3:
            print("  Suggestion: Perhaps this habit isn't aligned with your current routine. Let's revisit your motivation or try a different approach.")

    print("\n--- End of Insight ---")

if __name__ == "__main__":
    # Example usage: Track "Drink 8 Glasses of Water" for 7 days
    track_habit("Drink 8 Glasses of Water", num_days=7)
    print("\n" + "="*50 + "\n")
    # Another example: Track "Read 15 minutes" for 5 days
    track_habit("Read 15 minutes", num_days=5)

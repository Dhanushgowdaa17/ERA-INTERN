name = input("Enter your name: ")
daily_goal = input("Enter your daily goal: ")

with open("daily_goals.txt", "a") as file:
    file.write(f"{name}: {daily_goal}\n")   
    
print("Entry saved successfully!")
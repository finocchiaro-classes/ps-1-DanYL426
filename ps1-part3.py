def heart_rate(age,goal):
    max_HR = 220-age
    print(f"Your maximum heart rate is: {max_HR}")
    if goal == "S":
        minimum = float(max_HR*0.8)
        maximum = float(max_HR)
    if goal == "E":
        minimum = float(max_HR*0.6)
        maximum = float(max_HR*0.8)
    print(f"Your target heart rate is between {minimum} and {maximum}")
    
user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")
heart_rate(user_age,user_goal)

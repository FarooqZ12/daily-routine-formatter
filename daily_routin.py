print("welcome! to Your Daily Routin Formater")
print("--------------------------------------")

user_name = str(input("Your good name? "))
print("Pleae confirm your daily routine timing i will make a good formate for you.")

wake_up = float(input("Which time you wake up in morning? "))
study = float(input("Which time you start studying? "))
lunch_time = float(input("And your lunch time? "))
play_time = float(
    input("which time you playing cricket or something else? "))
sleep_time = float(input("and which time you go to bed for sleeping? "))
print("--------------------------------------------------")

print("You wakeup at ", wake_up, "AM")
print("And your study time is", study, "AM")
print("Your lunch time is", lunch_time, "PM")
print("Your playing at", play_time, "PM")
print("You go to bed for sleeping at", sleep_time, "PM")

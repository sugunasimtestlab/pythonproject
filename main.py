from sports import Sports

def main():
    my_sports = Sports("jerry", 50, 90)

    while True:
        user_input = input("Do you want to play the 3000 meter level? (yes/no) ")
        if user_input.strip().lower() == 'yes':
            my_sports.level()
        else:
            break

        user_input = input("Do you want to play the 5000 meter level? (yes/no) ")
        if user_input.strip().lower() == 'yes':
            my_sports.district()
        else:
            break

        user_input = input("Do you want to play the final match? (yes/no) ")
        if user_input.strip().lower() == 'yes':
            my_sports.state()
        else:
            break

        user_input = input("Do you want to increase stamina again by taking a meal? (yes/no) ")
        if user_input.strip().lower() == 'yes':
            meal_type = input("What type of meal? (light/heavy) ")
            my_sports.nutrition(meal_type)

        user_input = input("Do you want to rest to recover stamina? (yes/no) ")  # New feature: Rest
        if user_input.strip().lower() == 'yes':
            my_sports.rest() 

    my_sports.event_summary()

if __name__ == "__main__":
    main()

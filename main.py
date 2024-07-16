from sports import Sports

def main():
    my_sports = Sports("jerry", 50, 90)

    while True:
        user_input = input("Do you want to play the 3000 meter level? (yes/no) ")
        if user_input.strip().lower() == 'yes':
            my_sports.level()
        elif user_input.strip().lower() == 'train':
            my_sports.train()
        else:
            break

        user_input = input("Do you want to play the 5000 meter level? (yes/no) ")
        if user_input.strip().lower() == 'yes':
            my_sports.district()
        elif user_input.strip().lower() == 'train':
            my_sports.train()
        else:
            break

        user_input = input("Do you want to play the final match? (yes/no) ")
        if user_input.strip().lower() == 'yes':
            my_sports.state()
        elif user_input.strip().lower() == 'train':
            my_sports.train()
        else:
            break

        user_input = input("Do you want to increase stamina again by taking a meal? (yes/no) ")
        if user_input.strip().lower() == 'yes':
            meal_type = input("What type of meal? (light/heavy) ")
            my_sports.nutrition(meal_type)
        elif user_input.strip().lower() == 'train':
            my_sports.train()

    my_sports.event_summary()

if __name__ == "__main__":
    main()

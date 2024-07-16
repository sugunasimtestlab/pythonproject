class Sports:
    print("Welcome to the national sports meet!")

    def __init__(self, myplayer, stamina, speed=0):
        self.myplayer = myplayer
        self.stamina = stamina
        self.speed = speed
        self.completed_events = []

    def level(self):
        if 40 <= self.speed <= 60:
            self.stamina -= 25
            self.check_stamina()
        print(f"First {self.myplayer} played the 3000 meter run!")
        self.completed_events.append("3000 meter run")

    def district(self):
        if 60 <= self.speed <= 80:
            self.stamina -= 25
            self.check_stamina()
        print(f"Second {self.myplayer} played the 5000 meter run!")
        self.completed_events.append("5000 meter run")

    def state(self):
        if 80 <= self.speed <= 90:
            self.stamina -= 50
            self.check_stamina()
        print(f"Final match: {self.myplayer} played the 10000 meter run!")
        self.completed_events.append("10000 meter run")

    def nutrition(self, meal_type):
        if meal_type.lower() == 'light':
            self.stamina += 20
        elif meal_type.lower() == 'heavy':
            self.stamina += 50
        if self.stamina > 50:
            self.stamina = 50
        print(f"{self.myplayer} had a {meal_type} meal. Current stamina: {self.stamina}")

    def rest(self):
        self.stamina += 30
        if self.stamina > 50:
            self.stamina = 50
        print(f"{self.myplayer} took a rest. Current stamina: {self.stamina}")

    def event_summary(self):
        print(f"Player: {self.myplayer}")
        print(f"Current Stamina: {self.stamina}")
        print(f"Current Speed: {self.speed}")
        print("Summary of events completed:")
        for event in self.completed_events:
            print(f"- {event}")

    def check_stamina(self):
        if self.stamina <= 0:
            print(f"Sorry, {self.myplayer} is too tired.")
            self.training_or_play()

    def training_or_play(self):
        user_input = input("Do you need training or want to play the game? (training/play) ")
        if user_input.strip().lower() == 'training':
            self.stamina += 50
            print(f"{self.myplayer} has regained stamina. Current stamina: {self.stamina}")
        else:
            print(f"{self.myplayer} has lost the game.")
            exit()

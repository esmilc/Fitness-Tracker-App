class Workout:
    def __init__(self, name, muscle, duration):
        self.name = name
        self.muscle = muscle
        self.duration = duration

    def display(self):
        print(f"Workout Name: {self.name}\nMuscle Worked: {self.muscle}\nDuration of Workout: {self.duration}")

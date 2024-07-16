
class Workout:
    def __init__(self): #Removed duration, not needed at the moment, could be used for database
        self.name = None
        self.muscle = None
        self.diffuculty = None
        self.instructions = None

    def setName(self, name):
        self.name = name
    def setMuscle(self, muscle):
        self.muscle = muscle
    def setDifficulty(self, difficulty):
        self.difficulty = difficulty
    def setInstructions(self, instructions):
        if instructions == "":
            self.instructions = "Instructions are not supported for this workout at this time."
            return
        self.instructions = instructions






accepted_muscle_groups = ["abdominals", "abductors", "adductors", "biceps", "calves", "chest", "forearms", "glutes",
                 "hamstrings", "lats", "lower_back", "middle_back", "neck", "quadriceps", "traps", "triceps"]
accepted_difficulty = ["beginner", "intermediate", "expert"]
def json_to_list(json):
    toReturn = []
    for workouts in json:
        toAdd = Workout()
        toAdd.setName(workouts["name"])
        toAdd.setMuscle(workouts["muscle"])
        toAdd.setDifficulty(workouts["difficulty"])
        toAdd.setInstructions(workouts["instructions"])
        toReturn.append(toAdd)
    return toReturn


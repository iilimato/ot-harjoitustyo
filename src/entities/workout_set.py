class WorkoutSet:
    def __init__(self, workout_id, exercise_id, weight, reps, set_id=None):
        self.id = set_id
        self.workout_id = workout_id
        self.exercise_id = exercise_id
        self.weight = weight
        self.reps = reps

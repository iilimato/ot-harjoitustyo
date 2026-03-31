from datetime import date


class Workout:
    def __init__(self, workout_date=None, workout_id=None):
        self.id = workout_id
        self.date = workout_date or date.today()

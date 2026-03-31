from datetime import date
from entities.workout import Workout


class WorkoutRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, workout=None):
        workout = workout or Workout()
        cursor = self._connection.execute(
            "INSERT INTO workout (date) VALUES (?)",
            (str(workout.date),),
        )
        self._connection.commit()
        workout.id = cursor.lastrowid
        return workout

    def find_all(self):
        cursor = self._connection.execute("SELECT * FROM workout ORDER BY date DESC")
        return [
            Workout(date.fromisoformat(row["date"]), row["id"]) for row in cursor
        ]

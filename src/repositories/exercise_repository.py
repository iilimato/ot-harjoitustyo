from entities.exercise import Exercise


class ExerciseRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, exercise):
        cursor = self._connection.execute(
            "INSERT INTO exercise (name, muscle_group) VALUES (?, ?)",
            (exercise.name, exercise.muscle_group),
        )
        self._connection.commit()
        exercise.id = cursor.lastrowid
        return exercise

    def find_all(self):
        cursor = self._connection.execute("SELECT * FROM exercise")
        return [Exercise(row["name"], row["muscle_group"], row["id"]) for row in cursor]

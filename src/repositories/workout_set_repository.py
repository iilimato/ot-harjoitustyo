from entities.workout_set import WorkoutSet


class WorkoutSetRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, workout_set):
        cursor = self._connection.execute(
            "INSERT INTO workout_set (workout_id, exercise_id, weight, reps) "
            "VALUES (?, ?, ?, ?)",
            (
                workout_set.workout_id,
                workout_set.exercise_id,
                workout_set.weight,
                workout_set.reps,
            ),
        )
        self._connection.commit()
        workout_set.id = cursor.lastrowid
        return workout_set

    def find_by_workout(self, workout_id):
        cursor = self._connection.execute(
            "SELECT * FROM workout_set WHERE workout_id = ?", (workout_id,)
        )
        return [
            WorkoutSet(
                row["workout_id"],
                row["exercise_id"],
                row["weight"],
                row["reps"],
                row["id"],
            )
            for row in cursor
        ]

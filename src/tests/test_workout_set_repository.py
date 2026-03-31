import unittest
import sqlite3
from database import initialize_database, seed_exercises
from repositories.exercise_repository import ExerciseRepository
from repositories.workout_repository import WorkoutRepository
from repositories.workout_set_repository import WorkoutSetRepository
from entities.workout_set import WorkoutSet


class TestWorkoutSetRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        initialize_database(self.connection)
        seed_exercises(self.connection)

        self.exercise_repo = ExerciseRepository(self.connection)
        self.workout_repo = WorkoutRepository(self.connection)
        self.set_repo = WorkoutSetRepository(self.connection)

    def test_logged_set_is_saved_and_found(self):
        workout = self.workout_repo.create()
        exercise = self.exercise_repo.find_all()[0]

        self.set_repo.create(WorkoutSet(workout.id, exercise.id, 80.0, 8))

        sets = self.set_repo.find_by_workout(workout.id)
        self.assertEqual(len(sets), 1)

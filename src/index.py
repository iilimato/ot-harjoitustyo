from database import get_database_connection, initialize_database, seed_exercises
from repositories.exercise_repository import ExerciseRepository
from repositories.workout_repository import WorkoutRepository
from repositories.workout_set_repository import WorkoutSetRepository
from entities.workout_set import WorkoutSet


def show_exercises(exercises):
    for e in exercises:
        print(f"  {e.id}) {e.name} ({e.muscle_group})")


def log_session(exercises, workout_repo, set_repo):
    workout = workout_repo.create()
    print(f"\nUusi treeni aloitettu ({workout.date})")

    while True:
        print("\nValitse liike:")
        show_exercises(exercises)
        print("  0) Lopeta treeni")

        choice = input("\nValinta: ")

        if choice == "0":
            break

        try:
            exercise_id = int(choice)
            exercise = next(
                (e for e in exercises if e.id == exercise_id), None)
            if not exercise:
                print("Virheellinen valinta.")
                continue

            weight = float(input("Paino (kg): "))
            reps = int(input("Toistot: "))

            set_repo.create(WorkoutSet(workout.id, exercise.id, weight, reps))
            print(f"  Kirjattu: {exercise.name} {weight} kg x {reps}")

        except ValueError:
            print("Virheellinen syöte.")


def main():
    connection = get_database_connection()
    initialize_database(connection)
    seed_exercises(connection)

    exercise_repo = ExerciseRepository(connection)
    workout_repo = WorkoutRepository(connection)
    set_repo = WorkoutSetRepository(connection)

    exercises = exercise_repo.find_all()

    while True:
        print("\n1) Aloita treeni")
        print("0) Lopeta")

        choice = input("\nValinta: ")

        if choice == "1":
            log_session(exercises, workout_repo, set_repo)
        elif choice == "0":
            break


if __name__ == "__main__":
    main()

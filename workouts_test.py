import unittest, boto3
from workouts import Workout
from decimal import Decimal

class WorkoutsTest(unittest.TestCase):
    
    def setUp(self):
        # Set up sns client
        self.sns_client = boto3.client("sns")
        self.sns_event_topic = "new_exercise_test"
        self.sns_view_topic = "project_new_weight_test"

        # Set up dynamo db client
        self.dynamodb = boto3.resource('dynamodb')
        self.event_store_table_name = 'WorkoutEventStoreTest'
        self.view_store_table_name = 'WorkoutViewStoreTest'
        self.event_store_table = None
        self.view_store_table = None

        # set up workout object
        self.workout = Workout(self.sns_client, 
            self.sns_event_topic, 
            self.event_store_table, 
            self.sns_view_topic, 
            self.view_store_table)

    def test_get_next_weight_single(self):
        exercises = [{u'workout_name': u'Lower Body Workout', u'exercise_name': u'Back Squat', u'date_of_exercise': u'1492610400.0', u'weight': Decimal('40')}]
        next_weight = self.workout.get_next_weight(exercises)
        self.assertEqual(40, next_weight)

    def test_get_next_weight_different(self):
        exercises = [{u'workout_name': u'Lower Body Workout', u'exercise_name': u'Back Squat', u'date_of_exercise': u'1492610400.0', u'weight': Decimal('40')}, {u'workout_name': u'Lower Body Workout', u'exercise_name': u'Back Squat', u'date_of_exercise': u'1492819200.0', u'weight': Decimal('42.5')}]
        next_weight = self.workout.get_next_weight(exercises)
        self.assertEqual(42.5, next_weight)

    def test_get_next_weight_same(self):
        exercises = [{u'workout_name': u'Lower Body Workout', u'exercise_name': u'Back Squat', u'date_of_exercise': u'1492610400.0', u'weight': Decimal('40')}, {u'workout_name': u'Lower Body Workout', u'exercise_name': u'Back Squat', u'date_of_exercise': u'1492819200.0', u'weight': Decimal('40')}]
        next_weight = self.workout.get_next_weight(exercises)
        self.assertEqual(42.5, next_weight)

    def test_missing_workout_name(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set1_reps": 6,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)

    def test_invalid_workout_name(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "wibble",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set1_reps": 6,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)


    def test_missing_exercise_name(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set1_reps": 6,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)

    def test_invalid_exercise_name(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "test empty",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set1_reps": 6,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)


    def test_missing_date_of_exercise(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "weight": 50,
                "set1_reps": 6,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)

    def test_invalid_date_of_exercise(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-42",
                "weight": 50,
                "set1_reps": 6,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)


    def test_missing_weight(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "set1_reps": 6,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "weight": -5,
                "set1_reps": 6,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)


    def test_missing_set1_reps(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)

    def test_invalid_set1_reps(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set1_reps": -6,
                "set2_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)


    def test_missing_set2_reps(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set1_reps": 6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)

    def test_invalid_set2_reps(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set1_reps": 6,
                "set2_reps": -6,
                "set3_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)


    def test_missing_set3_reps(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set1_reps": 6,
                "set2_reps": 6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)

    def test_invalid_set3_reps(self):
        with self.assertRaises(ValueError) as context:
            exercise_details = {
                "workout_name": "Lower Body Workout",
                "exercise_name": "Back Squat",
                "date_of_exercise": "2017-04-22",
                "weight": 50,
                "set1_reps": 6,
                "set2_reps": 6,
                "set3_reps": -6
            }
            self.assertEqual(ValueError, context.expected)
            self.workout.new_exercise(exercise_details)


if __name__ == '__main__':
    unittest.main(exit=False)
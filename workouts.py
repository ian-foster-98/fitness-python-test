import boto3, datetime
from workout_definitions import definitions, increment_by_percentage

### TODO: error logging
### TODO: monitoring code (X-ray?)

class Workout(object):
    
    def __init__(self, 
        sns_client,
        sns_event_topic, 
        event_store_table, 
        sns_view_topic, 
        view_store_table):
        # cache to store lists of exercise events to avoid double-dipping to dynamo
        self.exercise_events = {}
        self.sns_client = sns_client
        self.sns_event_topic = sns_event_topic
        self.event_store_table = event_store_table
        self.sns_view_topic = sns_view_topic
        self.view_store_table = view_store_table

    def new_exercise(self, exercise_details):
        # check workout exists and is valid
        if not exercise_details.has_key('workout_name'):
            raise ValueError('workout_name not found in input.')
        if not definitions.has_key(exercise_details['workout_name']):
            raise ValueError('workout_name {} not found in workout definition.'.format(exercise_details['workout_name']))

        # check exercise name
        if not exercise_details.has_key('exercise_name'):
            raise ValueError('workout_name not found in input.')
        if not definitions[exercise_details['workout_name']].has_key(exercise_details['exercise_name']):
            raise ValueError('exercise_name {} not found in workout definition.'.format(exercise_details['exercise_name']))

        # check date/time
        if not exercise_details.has_key('date_of_exercise'):
            raise ValueError('date_of_exercise not found in input.')
        datetime.datetime.strptime(exercise_details['date_of_exercise'], '%Y-%m-%d')

        # check weight
        if not exercise_details.has_key('weight'):
            raise ValueError('exercise_name not found in input.')
        if exercise_details['weight'] < 0:
            raise ValueError('weight {} is not a valid weight.'.format(exercise_details['weight']))

        # check sets
        if not exercise_details.has_key('set1_reps'):
            raise ValueError('set1_reps not found in input.')
        if exercise_details['set1_reps'] < 0:
            raise ValueError('set1_reps {} is not a valid set.'.format(exercise_details['set1_reps']))
        if not exercise_details.has_key('set2_reps'):
            raise ValueError('set2_reps not found in input.')
        if exercise_details['set2_reps'] < 0:
            raise ValueError('set2_reps {} is not a valid set.'.format(exercise_details['set2_reps']))
        if not exercise_details.has_key('set3_reps'):
            raise ValueError('set3_reps not found in input.')
        if exercise_details['set3_reps'] < 0:
            raise ValueError('set3_reps {} is not a valid set.'.format(exercise_details['set3_reps']))

        # send message to SNS topic
        response = client.publish(
            TargetArn=self.sns_event_topic,
            Message=json.dumps(exercise_details)
        )

    def save_exercise_event(self, exercise_details):
        # save event to event store in DynamoDB
        pass

    def get_exercise_details(self, exercise_name, date_of_exercise):
        # get all exercise events up to last date

        # aggregate events to get latest state

        # return exercise details
        pass

    def get_next_weight(self, exercise_name):
        # get last two dates of this exercise

        # get exercise details for the two performances

        # work out next weight to perform and return value
        pass

    def set_next_exercise_weight(self, next_weight_details):
        # validate exercise details

        # send message to SNS topic
        pass

    def project_exercise_details(self, exercise_details):
        # save new weight value to view store
        pass

    def get_next_workout(self, workout_name):
        # find the weights for each excericse in the workout

        # return definition of workout
        pass

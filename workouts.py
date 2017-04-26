import boto3
import datetime
import json
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
        def exists(key):
            if not exercise_details.has_key(key):
                raise ValueError('{}} not found in input.'.format(key))
        def is_positive(key):
            if exercise_details[key] < 0:
                raise ValueError('{0} is not a valid {1}.'.format(exercise_details[key], key))


        # check workout exists and is valid
        exists('workout_name')
        if not definitions.has_key(exercise_details['workout_name']):
            raise ValueError('workout_name {} not found in workout definition.'.format(exercise_details['workout_name']))

        # check exercise name
        exists('exercise_name')
        if not definitions[exercise_details['workout_name']].has_key(exercise_details['exercise_name']):
            raise ValueError('exercise_name {} not found in workout definition.'.format(exercise_details['exercise_name']))

        # check date/time
        exists('date_of_exercise')
        datetime.datetime.strptime(exercise_details['date_of_exercise'], '%Y-%m-%d')

        # check weight
        exists('weight')
        is_positive('weight')

        # check sets
        exists('set1_reps')
        is_positive('set1_reps')
        exists('set2_reps')
        is_positive('set2_reps')
        exists('set3_reps')
        is_positive('set3_reps')

        # send message to SNS topic
        topic_arn = self.get_sns_topic(self.sns_event_topic)        
        response = self.sns_client.publish(
            TargetArn=topic_arn,
            Message=json.dumps(exercise_details)
        )

    def save_exercise_event(self, exercise_details):
        self.event_store_table.put_item( Item=exercise_details )

    def get_sns_topic(self, topic_name = '', next_token =''):
        topics_info = self.sns_client.list_topics(NextToken=next_token)
        topics = topics_info['Topics']
        arn = [topic for topic in topics if topic['TopicArn'].find(topic_name) > -1]
        if len(arn) > 0:
            return arn[0]['TopicArn']
        if 'NextToken' not in topics_info:
            return None
        return get_sns_topic(topic_name, topics_info['NextToken'])

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

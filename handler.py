import json
import boto3
import os
from workouts import Workout

# Set up sns client
sns_client = boto3.client("sns")
sns_event_topic = os.environ["EVENT_SNS_TOPIC"]
sns_view_topic = os.environ["VIEW_SNS_TOPIC"]

# Set up dynamo db client
dynamodb = boto3.resource('dynamodb')
event_store_table = dynamodb.Table(os.environ["EVENT_STORE_TABLE"])
view_store_table = dynamodb.Table(os.environ["VIEW_STORE_TABLE"])

# set up workout object
workout = Workout(sns_client, sns_event_topic, event_store_table, sns_view_topic, view_store_table)


###
# Exercise body consists of
# {
#   "exercise_name",
#   "date_of_exercise",
#   "workout_name",
#   "weight",
#   "set1_reps",
#   "set2_reps",
#   "set3_reps"
# }
###
def save_exercise(event, context):
    try:
        result = workout.new_exercise(event)
        return { "statusCode": 200 }
    except ValueError as e:
        return { "statusCode": 500, "body": json.dumps(e.message) }

def save_exercise_event(event, context):
    item = json.loads(event['Records'][0]['Sns']['Message'])
    try:
        result = workout.save_exercise_event(item)
        return { "statusCode": 200 }
    except ValueError as e:
        return { "statusCode": 500, "body": json.dumps(e.message) }

def project_exercise_details(event, context):
    print 'event = {}'.format(event)
    exercise_details = event['Records'][0]['dynamodb']['NewImage']
    try:
        result = workout.project_exercise_details(exercise_details)
        return { "statusCode": 200 }
    except ValueError as e:
        return { "statusCode": 500, "body": json.dumps(e.message) }

def save_exercise_view(event, context):
    item = json.loads(event['Records'][0]['Sns']['Message'])
    try:
        result = workout.save_exercise_view(item)
        return { "statusCode": 200 }
    except ValueError as e:
        return { "statusCode": 500, "body": json.dumps(e.message) }

def get_next_workout(event, context):
    workout_name = event['queryStringParameters']['workout_name']
    try:
        result = workout.get_next_workout(workout_name)
        return { "statusCode": 200, "body": json.dumps(result) }
    except ValueError as e:
        return { "statusCode": 500, "body": json.dumps(e.message) }

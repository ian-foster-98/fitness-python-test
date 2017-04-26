import json
import boto3
from workouts import Workout

# Set up sns client
sns_client = boto3.client("sns")
sns_event_topic = "new_exercise"
sns_view_topic = "project_new_weight"

# Set up dynamo db client
### TODO : Use environment variables to determine name of tables
dynamodb = boto3.resource('dynamodb', 
    endpoint_url="http://localhost:8000")
event_store_table = dynamodb.Table('Workout_event_store')
view_store_table = dynamodb.Table('Workout_view_store')

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
    # get relevant body from event
    exercise_details = {}

    # save exercise details
    workout.new_exercise(exercise_details)

    response = {
        "statusCode": 200,
        "body": json.dumps(exercise_details)
    }

    return response

def get_next_workout(event, context):
    # get workout name from event
    workout_name = ""

    # get workout details for given workout definition
    workout_details = workout.get_next_workout(workout_name)

    response = {
        "statusCode": 200,
        "body": json.dumps(workout_details)
    }

    return response

def project_exercise(event, context):
    body = {
        "message": "project_exercise",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


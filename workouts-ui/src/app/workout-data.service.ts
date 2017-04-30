import { Injectable } from '@angular/core';

@Injectable()
export class WorkoutDataService {

  constructor() { }

  workoutDefinitions()
  {
    return [
      {'name': 'Upper Body Workout'}, 
      {'name': 'Lower Body Workout'}
    ];
  }

  workoutDetails(workoutName: string)
  {
    return [
      {
        'exerciseName': 'Back Squat',
        'sets': [
          {
            'order': 1,
            'weight': '50'            
          },
          {
            'order': 2,
            'weight': '50'            
          },
          {
            'order': 3,
            'weight': '50'            
          }
        ]
      },
      {
        'exerciseName': 'Deadlift',
        'sets': [
          {
            'order': 1,
            'weight': '65'            
          },
          {
            'order': 2,
            'weight': '65'            
          },
          {
            'order': 3,
            'weight': '65'            
          }
        ]
      },
      {
        'exerciseName': 'Lunges',
        'sets': [
          {
            'order': 1,
            'weight': '12.5'            
          },
          {
            'order': 2,
            'weight': '12.5'            
          },
          {
            'order': 3,
            'weight': '12.5'            
          }
        ]
      },
      {
        'exerciseName': 'Overhead rows',
        'sets': [
          {
            'order': 1,
            'weight': '40'            
          },
          {
            'order': 2,
            'weight': '40'            
          },
          {
            'order': 3,
            'weight': '40'            
          }
        ]
      },
      {
        'exerciseName': 'Stiff-legged deadlift',
        'sets': [
          {
            'order': 1,
            'weight': '50'            
          },
          {
            'order': 2,
            'weight': '50'            
          },
          {
            'order': 3,
            'weight': '50'            
          }
        ]
      }
    ]
  }

  saveExercise(exercise)
  {
    return true;
  }
}

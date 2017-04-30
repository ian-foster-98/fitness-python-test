import { Injectable } from '@angular/core';
import { Exercise } from "app/shared/exercise.model";
import { ExerciseSet } from "app/shared/exerciseset.model";

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

  workoutDetails(workoutName: string): Exercise[]
  {
    let exercises:Exercise[] = [];

    let sets:ExerciseSet[] = new Array<ExerciseSet>();
    sets.push(new ExerciseSet(1, '50'));
    sets.push(new ExerciseSet(2, '50'));
    sets.push(new ExerciseSet(3, '50'));
    let exercise: Exercise = new Exercise('Back Squat', sets);
    exercises.push(exercise);

    sets = new Array<ExerciseSet>();
    sets.push(new ExerciseSet(1, '65'));
    sets.push(new ExerciseSet(2, '65'));
    sets.push(new ExerciseSet(3, '65'));
    exercise = new Exercise('Deadlift', sets);
    exercises.push(exercise);
    
    sets = new Array<ExerciseSet>();
    sets.push(new ExerciseSet(1, '12.5'));
    sets.push(new ExerciseSet(2, '12.5'));
    sets.push(new ExerciseSet(3, '12.5'));
    exercise = new Exercise('Lunges', sets);
    exercises.push(exercise);
    
    sets = new Array<ExerciseSet>();
    sets.push(new ExerciseSet(1, '40'));
    sets.push(new ExerciseSet(2, '40'));
    sets.push(new ExerciseSet(3, '40'));
    exercise = new Exercise('Overhead rows', sets);
    exercises.push(exercise);
    
    sets = new Array<ExerciseSet>();
    sets.push(new ExerciseSet(1, '50'));
    sets.push(new ExerciseSet(2, '50'));
    sets.push(new ExerciseSet(3, '50'));
    exercise = new Exercise('Stiff-legged deadlift', sets);
    exercises.push(exercise);

    return exercises;
  }

  saveExercise(exercise)
  {
    return true;
  }
}

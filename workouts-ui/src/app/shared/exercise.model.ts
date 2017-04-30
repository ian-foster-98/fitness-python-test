import { ExerciseSet } from "app/shared/exerciseset.model";

export class Exercise {
    exerciseName: string;
    sets: ExerciseSet[];

    constructor( exerciseName, sets )
    {
        this.exerciseName = exerciseName;
        this.sets = sets;
    }
}
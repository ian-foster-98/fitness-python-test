import { Component, OnInit } from "@angular/core";
import { WorkoutDataService } from '../workout-data.service';
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: "app-exercises",
  templateUrl: "./exercises.component.html",
  styleUrls: ["./exercises.component.css"]
})
export class ExercisesComponent implements OnInit {
  workoutDefinitionName: string = 'Workout to do';
  workoutDefinition = [];

  constructor(private workoutDataService:WorkoutDataService,
    private route: ActivatedRoute) 
  {
    this.route.params.subscribe( params => this.workoutDefinitionName = params['workout_name']);
  }

  ngOnInit() {
    this.workoutDefinition = this.workoutDataService.workoutDetails(this.workoutDefinitionName);
  }

}

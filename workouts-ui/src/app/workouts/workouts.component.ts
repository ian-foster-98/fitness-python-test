import { Component, OnInit } from '@angular/core';
import { WorkoutDataService } from '../workout-data.service';

@Component({
  selector: 'app-workouts',
  templateUrl: './workouts.component.html',
  styleUrls: ['./workouts.component.css']
})
export class WorkoutsComponent implements OnInit {
  workoutDefinitions = [];

  constructor(private workoutDataService:WorkoutDataService) { }

  ngOnInit() {
    this.workoutDefinitions = this.workoutDataService.workoutDefinitions();
  }

}

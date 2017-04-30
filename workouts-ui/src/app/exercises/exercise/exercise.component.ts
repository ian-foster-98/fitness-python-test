import { Component, OnInit, Input } from '@angular/core';
import { ExerciseSet } from "app/shared/exerciseset.model";

@Component({
  selector: 'app-exercise',
  templateUrl: './exercise.component.html',
  styleUrls: ['./exercise.component.css']
})
export class ExerciseComponent implements OnInit {
  @Input() exerciseName: string;
  @Input() exerciseSets: ExerciseSet[];

  constructor() { }

  ngOnInit() {
  }

}

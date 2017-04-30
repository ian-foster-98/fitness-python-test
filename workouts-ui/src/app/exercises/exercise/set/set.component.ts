import { Component, OnInit, Input } from '@angular/core';
import { ExerciseSet } from '../../../shared/exerciseset.model';

@Component({
  selector: 'app-set',
  templateUrl: './set.component.html',
  styleUrls: ['./set.component.css']
})
export class SetComponent implements OnInit {
  @Input() exerciseSet: ExerciseSet;

  constructor() { }

  ngOnInit() {
  }

}

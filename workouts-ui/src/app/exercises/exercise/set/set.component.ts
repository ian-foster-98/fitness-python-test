import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-set',
  templateUrl: './set.component.html',
  styleUrls: ['./set.component.css']
})
export class SetComponent implements OnInit {
  @Input() set;

  constructor() { }

  ngOnInit() {
  }

}

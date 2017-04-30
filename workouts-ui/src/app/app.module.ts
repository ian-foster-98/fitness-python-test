import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { WorkoutsComponent } from './workouts/workouts.component';
import { ExercisesComponent } from './exercises/exercises.component';
import { ExerciseComponent } from './exercises/exercise/exercise.component';
import { SetComponent } from './exercises/exercise/set/set.component';

import { WorkoutDataService } from './workout-data.service';

@NgModule({
  declarations: [
    AppComponent,
    WorkoutsComponent,
    ExercisesComponent,
    ExerciseComponent,
    SetComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot([
      {
        path: '',
        component: WorkoutsComponent
      },
      {
        path: 'exercises/:workout_name',
        component: ExercisesComponent
      }
    ])
  ],
  providers: [WorkoutDataService],
  bootstrap: [AppComponent]
})
export class AppModule { }

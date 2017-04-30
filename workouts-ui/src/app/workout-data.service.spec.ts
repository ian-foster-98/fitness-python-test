import { TestBed, inject } from '@angular/core/testing';

import { WorkoutDataService } from './workout-data.service';

describe('WorkoutDataService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [WorkoutDataService]
    });
  });

  it('should ...', inject([WorkoutDataService], (service: WorkoutDataService) => {
    expect(service).toBeTruthy();
  }));
});

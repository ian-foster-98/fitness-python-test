import { WorkoutsUiPage } from './app.po';

describe('workouts-ui App', () => {
  let page: WorkoutsUiPage;

  beforeEach(() => {
    page = new WorkoutsUiPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});

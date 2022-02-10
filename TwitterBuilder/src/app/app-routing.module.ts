import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EngageComponent } from './engage/engage.component';
import { TweetsComponent } from './Tweet/tweet.component';
import { UsersComponent } from './User/user.component';
import { CalendarComponent } from './calendar/calendar.component';

const routes: Routes = [
  { path: 'Tweets', component: TweetsComponent },
  { path: 'Users', component: UsersComponent },
  { path: 'Engage', component: EngageComponent },
  { path: 'Schedule', component: CalendarComponent },
  { path: 'Tweets/:searchTerm', component: TweetsComponent },
  { path: 'Users/:searchTerm', component: UsersComponent },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

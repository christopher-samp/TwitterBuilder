import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TweetsComponent } from './Tweet/tweet.component';
import { UsersComponent } from './User/user.component';

const routes: Routes = [
  { path: 'Tweets', component: TweetsComponent },
  { path: 'Users', component: UsersComponent },
  { path: 'Tweets/:searchTerm', component: TweetsComponent},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

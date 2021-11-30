import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { TweetsApiService } from './Tweet/Tweet-api.service';
import { Tweet } from './Tweet/Tweet.model';
import { UsersApiService } from './User/User-api.service'
import { User } from './User/User.model'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit, OnDestroy {
  ngOnInit(): void {
    throw new Error("Method not implemented.");
  }  ngOnDestroy(): void {
    throw new Error("Method not implemented.");
  }

  
}

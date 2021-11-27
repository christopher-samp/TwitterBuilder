import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { TweetsApiService } from './Tweet/Tweet-api.service';
import { Tweet } from './Tweet/Tweet.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'TwitterBuilder';
  TweetListSubs: Subscription;
  TweetList: Tweet[];

  constructor(private tweetsApi: TweetsApiService) {
    console.log("app component constructor")
  }

  ngOnInit() {
    console.log("init NG")
    this.TweetListSubs = this.tweetsApi
      .getTweets()
      .subscribe(res => {
        this.TweetList = res;
      },
        console.error
      );
  }

  ngOnDestroy() {
    this.TweetListSubs.unsubscribe();
  }
}

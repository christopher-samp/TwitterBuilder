import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { TweetsApiService } from './Tweet-api.service';
import { Tweet } from './Tweet.model';
import { ActivatedRoute } from '@angular/router';

@Component({
  templateUrl: './tweet.component.html'
})
export class TweetsComponent implements OnInit, OnDestroy {
  title = 'TwitterBuilder';
  TweetListSubs: Subscription = new Subscription();
  TweetListLeft: Tweet[];
  TweetListRight: Tweet[];

  constructor(private tweetsApi: TweetsApiService, private route: ActivatedRoute) {
    console.log("app component constructor")
  }

  ngOnInit() {
    console.log("init NG")
    this.route.params.subscribe(params => {

      if (params['searchTerm']) {
        this.TweetListSubs = this.tweetsApi
          .getTweets(params['searchTerm'])
          .subscribe(res => {
            this.TweetListLeft = res.slice(0, res.length / 2);
            this.TweetListRight = res.slice(res.length / 2, res.length);
            console.log(res);
          },
            console.error
        );
      }
    })
  }

  ngOnDestroy() {
    this.TweetListSubs.unsubscribe();
  }
}

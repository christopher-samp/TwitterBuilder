import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { TweetsApiService } from './Tweet-api.service';
import { Tweet } from './Tweet.model';
import { ActivatedRoute } from '@angular/router';
import { ScheduledTweet } from './ScheduledTweet.model';

@Component({
  templateUrl: './tweet.component.html'
})
export class TweetsComponent implements OnInit, OnDestroy {
  title = 'TwitterBuilder';
  TweetListSubs: Subscription = new Subscription();
  TweetListLeft: Tweet[];
  TweetListRight: Tweet[];
  tweet: ScheduledTweet;
  tweets: any[] = [];

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

  scheduleTweet(status: string, userid: string, date: string) {
    this.tweet = new ScheduledTweet(status, date, userid, "Single", 1);
    this.tweets.push(this.tweet);
    var jsonTweets = JSON.stringify(this.tweets);
    console.log(jsonTweets);
    this.tweetsApi.scheduleTweet(jsonTweets).subscribe();

    this.tweets = [] as ScheduledTweet[]
  }

  getDate() {
    var date = new Date();
    var dd = String(date.getDate()).padStart(2, '0');
    var mm = String(date.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = date.getFullYear();

    var today = mm + '/' + dd + '/' + yyyy;

    // document.getElementById('dateSelector')?.ariaValueText = today;
    console.log(today);
    return today;
  }

  ngOnDestroy() {
    this.TweetListSubs.unsubscribe();
  }
}

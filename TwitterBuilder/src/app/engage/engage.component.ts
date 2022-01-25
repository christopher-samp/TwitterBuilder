import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { EngageApiService } from './engage-api.service';
import { Tweet } from '../Tweet/Tweet.model';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-engage',
  templateUrl: './engage.component.html',
  styleUrls: ['./engage.component.sass']
})
export class EngageComponent implements OnInit, OnDestroy {
  EngageListSubs: Subscription = new Subscription();
  TweetList: Tweet[];
  retweetButtonValue: boolean;

  constructor(private engageApi: EngageApiService, private route: ActivatedRoute) {
    
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.EngageListSubs = this.engageApi
        .getRecentTweets('369867339')
        .subscribe(res => {
          console.log(this.TweetList)
          this.TweetList = res
          console.log(res);
        },
          console.error
        );
    });
  }

  replyToTweet(replyTweetId: string, status: string, username: string) {
    console.log(replyTweetId);
    console.log(status);
    console.log(`retweet value ${this.retweetButtonValue}`);
    var fullstatus: string;
    fullstatus = `@${username} ${status}`;
    this.engageApi.ReplyToTweet(replyTweetId, fullstatus, this.retweetButtonValue).subscribe();
  }

  removeFromWatchList(watchListUserId: string, userId: string) {
    this.engageApi.removeFromWatchList(watchListUserId, userId).subscribe();
  }

  public onSaveRetweetChanged(value: boolean) {
    this.retweetButtonValue = value;
  }

  ngOnDestroy() {
    this.EngageListSubs.unsubscribe();
  }
}

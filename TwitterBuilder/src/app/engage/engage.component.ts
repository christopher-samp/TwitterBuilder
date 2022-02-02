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
  retweetBox: boolean[] = [];
  tweetchars: number[] = [];
  tweetText: string[] = [];

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

  replyToTweet(replyTweetId: string, username: string, index: number) {
    console.log(replyTweetId);
    console.log(this.tweetText[index]);
    console.log(`retweet value ${this.retweetBox[index]}`);
    var fullstatus: string;
    fullstatus = `@${username} ${this.tweetText[index]}`;
    this.engageApi.ReplyToTweet(replyTweetId, fullstatus, this.retweetBox[index]).subscribe();
  }

  removeFromWatchList(watchListUserId: string, userId: string) {
    this.engageApi.removeFromWatchList(watchListUserId, userId).subscribe();
  }

  public onSaveRetweetChanged(value: boolean, index: number) {
    this.retweetBox[index] = value;
    console.log(this.retweetBox)
  }

  modelChangeFn(value: string, index: number) {
    console.log("modelChangeFn")
    this.tweetText[index] = value;
    console.log(this.tweetText[index]);
    this.tweetchars[index] = this.tweetText[index].length;
    var charCountLabel = document.getElementById('charcount'+index)
    if (charCountLabel) {
      charCountLabel.innerHTML = this.tweetchars[index] + "/280";
    }
  }

  ngOnDestroy() {
    this.EngageListSubs.unsubscribe();
  }
}

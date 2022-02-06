import { Component, ElementRef, QueryList, ViewChildren, OnInit, OnDestroy } from '@angular/core';
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
  tweets: any[] = [];
  tweetText: string[] = [""];
  tweetchars: number[] = [0];
  buttonClicked: boolean = true;

  @ViewChildren("tweetTextArea,charCountLabel") private children: QueryList<ElementRef>;


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

            this.TweetListLeft.sort((a, b) => (a.favorites > b.favorites ? -1 : 1));
            this.TweetListRight.sort((a, b) => (a.favorites > b.favorites ? -1 : 1));

            console.log(res);
          },
            console.error
        );
      }
    })

    // this._viewContainer.createEmbeddedView(this.tweetBoxesTemplate)

  }

  scheduleTweet(userid: string, date: string) {
    var isThread = "";
    if (this.children.length > 2) {
      isThread = "Thread";
    }
    else {
      isThread = "Single";
    }

    var tweetNumber = 1;
    var tweetText = "";
    for (let i = 0; i < this.children.length; i = i + 2) {
      tweetText = this.children.get(i)!.nativeElement.value;
      if (tweetText.length > 280) {
        this.tweets = [] as ScheduledTweet[];
        alert("Ensure Tweets Are Under 280 Character limit!");
        return;
      }
      this.tweets.push(new ScheduledTweet(tweetText, date, userid, isThread, tweetNumber));
      tweetNumber++;
    }
    
    var jsonTweets = JSON.stringify(this.tweets);
    console.log(jsonTweets);
    this.tweetsApi.scheduleTweet(jsonTweets).subscribe(res => {
      if (res == 200) {
        this.tweets = [] as ScheduledTweet[]
        this.tweetText = [""] as string[];
        this.tweetchars = [0] as number[];
        this.children.get(0)!.nativeElement.value = "";
        this.children.get(1)!.nativeElement.innerHTML = "0/280";
        alert("Tweet Scheduled!");
      }
      else {
        this.tweets = [] as ScheduledTweet[]
        alert("Tweet Failed To Scheudule.")
      }
    });

    
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

  addTextArea() {
    console.log("aqui")
    this.tweetText.push("");
    this.tweetchars.push(0);
  }

  modelChangeFn(value: string, index: number) {
    console.log("modelChangeFn")
    this.children.get((index * 2))!.nativeElement.value = value;
    this.children.get((index * 2) + 1)!.nativeElement.innerHTML = value.length + "/280";
  }


  ngOnDestroy() {
    this.TweetListSubs.unsubscribe();
  }
}

import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { ScheduledTweet } from '../Tweet/ScheduledTweet.model';
import { CalendarApiService } from './calendar-api.service';

@Component({
  selector: 'app-calendar',
  templateUrl: './calendar.component.html',
  styleUrls: ['./calendar.component.sass']
})
export class CalendarComponent implements OnInit {
  scheduledTweets: ScheduledTweet[];
  ScheduledTweetsSubs: Subscription = new Subscription();


  constructor(private calendarApi: CalendarApiService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.ScheduledTweetsSubs = this.calendarApi
        .getScheduledTweets('369867339')
        .subscribe(res => {
          this.scheduledTweets = res
          console.log(this.scheduledTweets[0].tweetContent)

        },
          console.error
        );
    });
  }


  ngOnDestroy() {
    this.ScheduledTweetsSubs.unsubscribe();
  }

}

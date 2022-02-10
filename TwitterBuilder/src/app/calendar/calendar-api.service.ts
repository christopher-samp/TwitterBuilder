import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { ScheduledTweet } from '../Tweet/ScheduledTweet.model';

@Injectable()
export class CalendarApiService {

  constructor(private http: HttpClient) {

  }

  _handleError(err: HttpErrorResponse | any) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  getScheduledTweets(userId: string): Observable<ScheduledTweet[]> {
    console.log("getting scheduled tweets")
    let parameters = new HttpParams()
      .set('userId', userId);
    
    return this.http.get<ScheduledTweet[]>(`http://127.0.0.1:5000/GetScheduledTweets`, { params: parameters }).pipe(catchError(this._handleError));
  }
}
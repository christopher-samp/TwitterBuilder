import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpErrorResponse, HttpResponse } from '@angular/common/http';
import { Observable, throwError} from 'rxjs';
import { API_URL } from '../env';
import { Tweet } from './Tweet.model';
import { catchError, map} from 'rxjs/operators';

@Injectable()
export class TweetsApiService {

  constructor(private http: HttpClient) {
  }

  _handleError(err: HttpErrorResponse | any) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getTweets(searchTerm: string): Observable<Tweet[]> {
    console.log("getting tweets")
    return this.http.get<Tweet[]>(`http://127.0.0.1:5000/GetTweets/${searchTerm}`).pipe(catchError(this._handleError));
  }

  scheduleTweet(tweets: string): Observable<any> {
    console.log("Sending ScheduleTweet Request")
    let parameters = new HttpParams()
      .set('tweets', tweets);

    return this.http.get<any>('http://127.0.0.1:5000/ScheduleTweet', { params: parameters }).pipe(catchError(this._handleError)).pipe(map(data => {

      console.log("Here will be return response code Ex :200", data.success)
      return data.success
    }));
  }
}


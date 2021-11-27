import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError} from 'rxjs';
import { API_URL } from '../env';
import { Tweet } from './Tweet.model';
import { catchError } from 'rxjs/operators';

@Injectable()
export class TweetsApiService {

  constructor(private http: HttpClient) {
  }

  _handleError(err: HttpErrorResponse | any) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getTweets(): Observable<Tweet[]> {
    console.log("getting tweets")
    return this.http.get<Tweet[]>(`http://127.0.0.1:5000/recent`).pipe(catchError(this._handleError));
  }
}


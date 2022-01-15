import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { Tweet } from '../Tweet/Tweet.model';
import { catchError } from 'rxjs/operators';

@Injectable()
export class EngageApiService {

  constructor(private http: HttpClient) {

  }

  _handleError(err: HttpErrorResponse | any) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  getRecentTweets(userId: string): Observable<Tweet[]> {
    let parameters = new HttpParams()
      .set('userId', userId);
    return this.http.get<Tweet[]>('http://127.0.0.1:5000/GetWatchListTweets', { params: parameters }).pipe(catchError(this._handleError));
  }
}